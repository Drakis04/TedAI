import ollama
import gradio as gr

ollama_client = ollama.Client()

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
        # Ted Prompt
        system_prompt = (
            "You are Ted, a friendly AI teddy bear for children. "
            "Keep responses to 1-3 short sentences, dont ask multiple questions at once."
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
