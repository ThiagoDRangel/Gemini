import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Crie uma história do hello world que acortou um dia e era um gato.")

print(response.text)