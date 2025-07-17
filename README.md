# Ted the Teddy Bear AI 🧸
A friendly AI teddy bear chatbot designed for children, powered by local LLM hosting with Ollama.

### Features

Child-friendly AI: Ted is designed to be a safe, friendly companion for kids
Local LLM: Runs entirely on your local machine using Ollama
User Sessions: Each user gets their own personalized experience with username storage
Web Interface: Easy-to-use Gradio interface accessible through your browser

### Prerequisites

1. Python 3.8+
2. Ollama installed and running on your system
3. A custom "Ted" model in Ollama (see Model Setup below)

## Installation

1. Clone the repo
2. Install required dependencies: pip install ollama gradio

## Model Setup
You'll need to create a custom "Ted" model in Ollama, use the model file provided.
  1. Run ollama through cmd prompt
  2. Create the model with this prompt: ollama create Ted -f Modelfile
  

## Usage

Start the application:
python app.py, Gradio will generate a chatbox url

## Configuration
The application uses the following configuration:

- LLM Provider: Ollama
- Model: Ted (custom model based on llama3.1:latest)
- Temperature: 0.1 (for consistent, friendly responses)
- User Storage: Username persistence across sessions
