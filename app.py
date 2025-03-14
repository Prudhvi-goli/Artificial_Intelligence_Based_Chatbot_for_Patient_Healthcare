from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import pickle
import random
import spacy

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# Load Trained Chatbot Model
model = tf.keras.models.load_model("healthcare_chatbot.h5")

# Load Data
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

# Define Intents
intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey", "Good day"],
            "responses": ["Hello! How can I assist you today?", "Hi there! How can I help?"]
        },
        {
            "tag": "symptoms",
            "patterns": ["I have a headache", "I'm feeling dizzy", "I have a fever"],
            "responses": ["I'm sorry to hear that. You should rest and stay hydrated. Would you like me to suggest some remedies?"]
        },
        {
            "tag": "appointment",
            "patterns": ["I need to book a doctor", "Can I schedule an appointment?"],
            "responses": ["Sure! I can help you book an appointment. What time works for you?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye"],
            "responses": ["Goodbye! Take care.", "See you soon!"]
        }
    ]
}

# Preprocessing Functions
def clean_up_sentence(sentence):
    """Tokenize and lemmatize sentence."""
    doc = nlp(sentence)
    return [token.lemma_.lower() for token in doc if token.is_alpha]

def bag_of_words(sentence, words):
    """Convert a sentence into a bag-of-words array."""
    sentence_words = clean_up_sentence(sentence)
    bag = [1 if word in sentence_words else 0 for word in words]
    return np.array(bag)

def predict_class(sentence):
    """Predict intent using trained model."""
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [{"intent": classes[i], "probability": str(r)} for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x["probability"], reverse=True)
    return results

def get_response(intents_list, intents_json):
    """Retrieve a response based on predicted intent."""
    if not intents_list:
        return "I'm sorry, I don't understand your question."

    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Flask Setup
app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Process user message and return a chatbot response."""
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Error: No message received."})

    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Ensure it runs on port 5000
