// content.js

$("td.title").on("click", function() {
    var title = $(this).text();
    console.log(title);
    chrome.runtime.sendMessage({"message": "add_title", "title": title});
});

