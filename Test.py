import ollama
import gradio as gr
import os
from mem0 import Memory
os.environ["OPENAI_API_KEY"] = "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"

# Configure mem0 for local LLM
config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama3.1:latest",
            "temperature": .1,
        }
    },
}

try:
    memory = Memory.from_config(config)
    ollama_client = ollama.Client()
    print("Memory system initialized successfully!")
except Exception as e:
    print(f"Error initializing memory: {e}")
    memory = None
    ollama_client = ollama.Client()

## Update memory -> m.update( mem id / data)
## Search memory -> m.serach (query, id)
## Delete memory -> m.delete (mem id)
## Get memory history -> m.history (message id)

# Goal - create session ID with gradio, create individuality with each session
with gr.Blocks() as demo:
    username = gr.Textbox(label="Username")
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    user = gr.BrowserState("")

    @gr.on([username.change], inputs= username , outputs= user)
    def save_to_local_storage(test):
        return test

    @demo.load(inputs=user, outputs=username)
    def load_from_local_storage(saved_value):
        print("loading from local storage", saved_value)
        return saved_value

    def tedresponse(message , chathist, userstate):
        client = ollama.Client()
        model = "Ted"

        # Ted Prompt
        system_prompt = (
            "You are Ted, a friendly AI teddy bear for children. "
            "Always speak kindly and avoid discussing any sensitive, harmful, or adult topics.\n\n"
        )

        # Use browserstate to save a username inputed
        nameprompt = (f"You are speaking to {userstate}")

        full_prompt = system_prompt + nameprompt + message
        response = ollama_client.generate(model="Ted", prompt=full_prompt)

        chathist.append({"role": "user" , "content": message})
        chathist.append({"role": "assistant", "content": response['response']})

        return '', chathist , userstate

    msg.submit(tedresponse, [msg, chatbot, user], [msg, chatbot, user])

demo.launch()
