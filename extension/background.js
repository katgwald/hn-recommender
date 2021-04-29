chrome.runtime.onMessage.addListener(
        function(request, sender, sendResponse) {
            if (request.message == "add_title") {
                console.log("adding title: ", request.title);
                //TODO add write to storage
                var xhr = new XMLHttpRequest();
                xmlhttp.open("POST", "http://localhost:8080/teamkat/hnpredictor/1.0.0/articles");
                xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xmlhttp.send(JSON.stringify({ url: "www.test2.com", title: request.title  }));
            }
        }
    );
