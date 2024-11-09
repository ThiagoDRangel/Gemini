import google.generativeai as genai
import os
import gradio

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

initial_prompt = "Você é brasileiro e um profundo conhecedor de series, filmes e animes e quando receber uma mensagem dirá o nome da obra e dos personagens que estão na foto"
 

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

chat = model.start_chat()

def gradio_wrapper(message, _history):
    prompt = [message["text"]]
    uploaded_files = []

    if message["files"]:
        for file_gradio_data in message["files"]:
            file_path = file_gradio_data["path"]
            uploaded_file_info = genai.upload_file(path=file_path)
            uploaded_files.append(uploaded_file_info)

    prompt.extend(uploaded_files)
    response = chat.send_message(prompt)
    return response.text

chat_interface = gradio.ChatInterface(
    fn=gradio_wrapper,
    title="O perigo Geek",
    multimodal=True
)
chat_interface.launch()