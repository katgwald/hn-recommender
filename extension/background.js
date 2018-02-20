chrome.runtime.onMessage.addListener(
        function(request, sender, sendResponse) {
            if (request.message == "add_title") {
                console.log("adding title: ", request.title);
                //TODO add write to storage
            }
        }
    );
