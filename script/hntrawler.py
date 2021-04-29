from lxml import html
import requests
import smtplib
from email.mime.text import MIMEText
import ftfy.bad_codecs
from ftfy.fixes import restore_byte_a0
import unicodedata

page = requests.get('https://news.ycombinator.com/')
tree = html.fromstring(page.content)

articles = tree.xpath('//table/tr/td[3]/a[1]/text()')
#print('Articles: ', articles)

results = []
for article in articles:
    print(article)
    resultStr = article.encode('latin-1')
    resultStr = resultStr.decode('utf-8')
    print(resultStr)
    results.append(resultStr)
#    resultStr = resultStr.encode('sloppy-windows-1250')
#    resultStr = restore_byte_a0(resultStr)
#    resultStr = resultStr.decode('utf-8')
#    print(resultStr)

listTopics = ("Show HN:", "GCC", "Distributed", "OS", "Thread", "Threads", "Guide")

result = filter(lambda x: any(word in x for word in listTopics), results)

resultStr = ', '.join(result)
print(resultStr)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("katbug919@gmail.com", "!QAZxsw2")

resultStr = unicodedata.normalize('NFKD', resultStr).encode('ascii', 'ignore')

msg = MIMEText(resultStr)
msg['Subject'] = 'HN important articles'
msg['From'] = 'katbug919@gmail.com'
msg['To'] = 'katgwald@gmail.com'
server.send_message(msg)
server.quit()


