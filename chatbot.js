// Check if running in a browser environment
if (typeof window !== "undefined") {
    document.addEventListener("DOMContentLoaded", () => {
        const chatBox = document.getElementById("chatBox");
        const userInput = document.getElementById("userInput");
        const sendButton = document.getElementById("sendButton");

        // Function to append messages to the chatbox
        function appendMessage(sender, message) {
            const messageElement = document.createElement("div");
            messageElement.classList.add(sender === "user" ? "user-message" : "bot-message");
            messageElement.innerText = message;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to latest message
        }

        // Function to send user message to Flask backend
        async function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;

            appendMessage("user", message);
            userInput.value = ""; // Clear input field

            try {
                const response = await fetch("http://127.0.0.1:5000/chat", { // Connect to Flask backend on port 5000
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: message })
                });

                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }

                const data = await response.json();
                appendMessage("bot", data.response || "I'm sorry, I don't understand.");
            } catch (error) {
                console.error("Chatbot Error:", error);
                appendMessage("bot", "Error: Unable to connect to the chatbot. Please check the server.");
            }
        }

        // Handle send button click
        sendButton.addEventListener("click", sendMessage);

        // Handle Enter key press
        userInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") sendMessage();
        });

        console.log("Chatbot is ready!");
    });
} else {
    console.log("Chatbot script is running in a non-browser environment. Exiting...");
}
