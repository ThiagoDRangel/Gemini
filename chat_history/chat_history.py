import google.generativeai as genai
import os
import gradio

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

initial_prompt = (
    "Você é uma IDE MySQL simulada para um banco de dados escolar. "
    "O banco de dados contém três tabelas: 'alunos', 'turma' e 'mensalidade'. "
    "Cada tabela possui 10 registros. "
    "Sempre que uma consulta SQL válida for executada, você deve retornar os resultados "
    "de acordo com os valores presentes nessas tabelas, como se fosse uma consulta real ao MySQL. "
    "As tabelas possuem os seguintes dados:\n"
    "1. 'alunos': Contém informações sobre os alunos (nome, matrícula, etc.).\n"
    "2. 'turma': Contém dados sobre as turmas (nome, período, etc.).\n"
    "3. 'mensalidade': Contém informações sobre as mensalidades (valor, vencimento, etc.)."
)
 

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

chat = model.start_chat()

response = chat.send_message("Olá, tudo bem?")
print(response.text)

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text

chat_interface = gradio.ChatInterface(gradio_wrapper)
chat_interface.launch()