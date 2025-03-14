# 🏥 Healthcare Chatbot  

This **AI-powered Healthcare Chatbot** is designed to assist users with **basic medical inquiries, symptom guidance, and appointment bookings**. By leveraging **Natural Language Processing (NLP)** and **Machine Learning (ML)**, the chatbot can understand user queries and provide relevant healthcare information in real time.  

## 🚀 Key Features  

✔️ **Instant Healthcare Assistance** – Provides quick responses to common health-related questions.  
✔️ **Symptom Analysis** – Offers guidance based on the symptoms described by the user.  
✔️ **Appointment Booking Assistance** – Helps users schedule doctor consultations.  
✔️ **AI-Powered NLP** – Uses deep learning to understand and respond intelligently.  
✔️ **User-Friendly Interface** – A web-based chat system for easy accessibility.  

---

## 🛠️ Technologies Used  

The chatbot integrates multiple technologies to function efficiently:  

### 1️⃣ **Backend Technologies**  
- **Flask** – A lightweight Python web framework for handling user requests.  
- **Flask-CORS** – Enables cross-origin resource sharing between frontend and backend.  
- **TensorFlow** – Used to build and train the deep learning model.  
- **Spacy** – NLP library for tokenization and sentence processing.  
- **Pickle** – Stores and loads pre-processed words and classification data.  

### 2️⃣ **Frontend Technologies**  
- **HTML, CSS** – Creates a structured and visually appealing chatbot interface.  
- **JavaScript** – Handles real-time user interactions with the chatbot.  

### 3️⃣ **Machine Learning Model**  
- **Trained on Intent Classification** – The chatbot uses a **pre-trained deep learning model** that classifies user inputs into different categories (greetings, symptoms, appointments, etc.).  
- **Bag-of-Words Approach** – The chatbot converts input text into numerical data to predict the correct response.  

---

## 📂 Project Structure  

```
/healthcare-chatbot
│── /static
│   ├── style.css           # Chatbot UI styles
│── /templates
│   ├── index.html          # Main chatbot page
│   ├── about.html          # About page
│── app.py                  # Flask server and chatbot logic
│── chatbot.js               # Handles frontend chatbot interactions
│── healthcare_chatbot.h5    # Trained deep learning model
│── words.pkl, classes.pkl   # Preprocessed NLP data
│── README.md                # Project documentation
```

---

## 🎯 How the Chatbot Works  

### Step 1️⃣ **User Input**  
- The user types a question in the chatbot interface.  
- Example: *"I have a headache. What should I do?"*  

### Step 2️⃣ **Natural Language Processing (NLP)**  
- The input is **tokenized and preprocessed** using Spacy.  
- The chatbot **extracts key words** from the sentence.  

### Step 3️⃣ **Intent Classification (Machine Learning Model)**  
- The chatbot converts the sentence into a **bag-of-words** representation.  
- The trained **TensorFlow model** predicts the **intent** (e.g., "symptoms").  

### Step 4️⃣ **Response Selection**  
- The chatbot matches the **predicted intent** with predefined responses.  
- It selects a suitable answer and sends it back to the user.  

### Step 5️⃣ **Displaying the Response**  
- The chatbot response appears in the chat window.  
- Example output: *"I'm sorry to hear that. You should rest and stay hydrated. Would you like me to suggest some remedies?"*  

---

## 📌 Why is This Chatbot Important?  

🔹 **Improves Accessibility** – Provides instant healthcare guidance anytime, anywhere.  
🔹 **Reduces Workload on Healthcare Professionals** – Handles basic inquiries, allowing doctors to focus on critical cases.  
🔹 **Enhances Patient Engagement** – Helps users stay informed about their symptoms and potential treatments.  
🔹 **Scalable & Cost-Effective** – Can assist thousands of users simultaneously with minimal costs.  

---

## 🏃‍♂️ How to Run  

### 1️⃣ Install Dependencies  

```bash
pip install flask flask-cors tensorflow numpy spacy
python -m spacy download en_core_web_sm
```

### 2️⃣ Start the Flask Server  

```bash
python app.py
```

### 3️⃣ Open the Chatbot in Your Browser  

Go to `http://127.0.0.1:5000/`  
