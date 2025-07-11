# Ted the Teddy Bear AI 🧸
A friendly AI teddy bear chatbot designed for children, powered by local LLM hosting with Ollama.
Features
	•	Child-friendly AI: Ted is designed to be a safe, friendly companion for kids
	•	Local LLM: Runs entirely on your local machine using Ollama
	•	User Sessions: Each user gets their own personalized experience with username storage
	•	Web Interface: Easy-to-use Gradio interface accessible through your browser
Prerequisites
	•	Python 3.8+
	•	Ollama installed and running on your system
	•	A custom “Ted” model in Ollama (see Model Setup below)
Installation
	1.	Clone the repo
	2.	Install required dependencies: pip install gradio ollama
Model Setup
    Use the modelfile to create a custom Ted model
    ollama create Ted -f modelfile
Usage
	1.	Start the application:
    python app.py
    2.  Open your browser and go to http://localhost:7860
	3.	Enter a username to personalize the experience
	4.	Start chatting with Ted!
Configuration
The application uses the following configuration:
	•	LLM Provider: Ollama
	•	Model: Ted (custom model based on llama3.1:latest)
	•	Temperature: 0.1 (for consistent, friendly responses)
	•	User Storage: Username persistence across sessions
