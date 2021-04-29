import connexion
import six
import sqlite3
import os.path

from swagger_server.models.article import Article  # noqa: E501
from swagger_server import util



def add_article(article=None):  # noqa: E501
    """adds a chosen article

    Adds an article to the system # noqa: E501

    :param article: Article to add
    :type article: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        article = Article.from_dict(connexion.request.get_json())  # noqa: E501
    print(article)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "articles.db")


    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("insert into articles (title, url) values (?, ?)", (article.title, article.url) )
    
    words = article.title.split()
    
    for word in words:
        if len(word) < 5:
            continue
        c.execute("select word, frequency from frequencies where word=?", (word,))
        data = c.fetchone()
        if data is None:
            c.execute("insert into frequencies (word, frequency) values (?, ?)", (word, 1) )
        else:
            f = data[1]
            c.execute("update frequencies set frequency=? where word=?", (f + 1, word) )


        


    conn.commit()
    conn.close()

    return 'do some magic!'
