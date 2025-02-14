Hi, I am happy to start this project. 9:40 10/12/2024
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/style.css">
    <title>Gemini AI Chat</title>
    <style>
        .algoai {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        
        .chatai-container {
            width: 80vw;
            height: 80vh;
            background-color: black;
            opacity: 0.8;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
        }
        
        .chatai-box {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
            margin-bottom: 10px;
            scrollbar-width: none;
        }
        
        .chatai-box::-webkit-scrollbar {
            display: none;
        }
        
        .message {
            margin: 5px 0;
            padding: 8px;
            border-radius: 5px;
        }
        
        .user {
            color: rgb(226, 213, 213);
            text-align: right;
        }
        
        .ai {
            color: rgb(226, 213, 213);
            text-align: left;
        }
        
        .input-container {
            position: sticky;
            bottom: 0;
            left: 0;
            display: flex;
            width: 100%;
            background: rgb(0, 0, 0);
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        
        input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 5px;
            outline: none;
            font-size: 1rem;
            background-color: #000000;
            color: white;
            caret-color: white;
        }
        
        button {
            padding: 12px 15px;
            background: rgb(109, 37, 37);
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            font-size: 1rem;
            transition: background 0.3s ease-in-out;
        }
        
        button:hover {
            background: rgb(75, 14, 14);
        }
        
        h1 {
            color: rgb(232, 166, 166);
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="main">
        <video class="background-video h-auto" muted loop autoplay plays-inline>
            <source src="/static/ALGOVisualizer.mp4" type="video/mp4">
        </video>
        <div class="algoai">
            <div class="chatai-container">
                <h1>WELCOME TO ALGOAI</h1>
                <div class="chatai-box" id="chatai-box"></div>
                <div class="input-container">
                    <input type="text" id="user-input" placeholder="Type a message..." onkeypress="handleKeyPress(event)">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        function sendMessage() {
            let userInput = document.getElementById("user-input").value.trim();
            if (userInput === "") return;
        
            let chatBox = document.getElementById("chatai-box");
        
          
            let userMessage = `<div class='message user'><strong>You:</strong> ${userInput}</div>`;
            chatBox.innerHTML += userMessage;
            document.getElementById("user-input").value = "";
        
            fetch("/ai_chat/", {  
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `message=${encodeURIComponent(userInput)}`
            })
            .then(response => response.json())
            .then(data => {
                
                let formattedResponse = data.reply.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")  
                                                 .replace(/\*(.*?)\*/g, "<em>$1</em>")             
                                                 .replace(/\n/g, "<br>");                           
        
                let aiMessage = `<div class='message ai'><strong>AI:</strong> ${formattedResponse}</div>`;
                chatBox.innerHTML += aiMessage;
        
                chatBox.scrollTop = chatBox.scrollHeight;
            })
            .catch(error => console.error("Error:", error));
        }
        
    </script>
</body>
</html>

