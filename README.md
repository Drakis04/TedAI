# Ted the Teddy Bear AI 🧸

A friendly AI teddy bear chatbot designed for children, powered by local LLM hosting with Ollama.

## Features

- **Child-friendly AI**: Ted is designed to be a safe, friendly companion for kids
- **Local LLM**: Runs entirely on your local machine using Ollama
- **User Sessions**: Each user gets their own personalized experience with username storage
- **Web Interface**: Easy-to-use Gradio interface accessible through your browser

## Prerequisites

- Python 3.8+
- Ollama installed and running on your system
- A custom "Ted" model in Ollama (see Model Setup below)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Drakis04/TedAI
cd ted-teddy-bear-ai
```

2. Install required dependencies:
```bash
pip install ollama gradio
```

## Model Setup

You'll need to create a custom "Ted" model in Ollama. Create a `Modelfile` with your Ted personality:

```dockerfile
FROM llama3.1:latest

PARAMETER temperature 0.1

SYSTEM """
You are Ted, a friendly AI teddy bear for children. 
Always speak kindly and avoid discussing any sensitive, harmful, or adult topics.
You are patient, encouraging, and love to help children learn and have fun.
Keep your responses appropriate for children and always maintain a warm, caring tone.
"""
```

Then create the model:
```bash
ollama create Ted -f Modelfile
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and go to `http://localhost:7860`

3. Enter a username to personalize the experience

4. Start chatting with Ted!

## Configuration

The application uses the following configuration:
- **LLM Provider**: Ollama
- **Model**: Ted (custom model based on llama3.1:latest)
- **Temperature**: 0.1 (for consistent, friendly responses)
- **User Storage**: Username persistence across sessions

## Safety Features

- Child-friendly prompting to avoid inappropriate content
- Local hosting for privacy and security
- No external data sharing for complete privacy

## Acknowledgments

- Built with [Ollama](https://ollama.ai/) for local LLM hosting
- Uses [Gradio](https://gradio.app/) for the web interface
