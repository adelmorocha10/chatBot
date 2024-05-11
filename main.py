import google.generativeai as genai
from google.generativeai.types import safety_types
GOOGLE_API_KEY="AIzaSyAvH9DzLA9qAXOKJff4B3nRX3UPluGuXWw"
genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Qual a capital do Espirito Santo?")
# print(response.text)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

generation_config = {
  "candidate_count": 1,  # Gera 5 candidatos por palavra/frase (maior diversidade)
  "temperature": 0,   # Temperatura moderada para criatividade e coerência
  # "top_p": 0.95,       # Favorece palavras mais comuns (melhor fluidez)
  # "presence_penalty": 0.3,  # Penaliza repetições com moderacão
  # "stop_tokens": ["fim", "ponto final"],  # Marcam o fim da geração
  # "do_sample": False,     # Amostragem para maior rapidez (textos curtos/informais)
  # "eos_token": ".",       # Define o token de fim de frase
}

safety_settings = {
  "HARASSMENT": "BLOCK_NONE",
  "HATE": "BLOCK_NONE",
  "SEXUAL": "BLOCK_NONE",
  "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel (
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  safety_settings=safety_settings)

# response = model.generate_content("Qual a capital do Espirito Santo?")
# print(response.text)

chat = model.start_chat(history=[])
print ("-----SHOW DE PERGUNTAS-----", "\n")
nome = input("Qual o seu nome? ")
print ("\nBem vido ao Show de Perguntas ", nome, "\n")
tema = input("Qual tema voce quer aprender hoje? ")
print ("\nMuito bom, adoro essinar sobre ", tema, "\n")

continuar = True

while continuar:
  pergunta = "Me faça uma pergunta com três escolhas, com o tema: ", tema
  iaChat = chat.send_message(pergunta)
  print(iaChat.text, "\n")
  resposta = input("Digite a resposta por extenso ou 'fim' para encerrar: ")
  if resposta.lower() == 'fim':
    continuar = False
  else:  
    resCorreta = "A resposta é: ", resposta, ".Se eu estiver errado me corrija"
    iaChat = chat.send_message(resCorreta)
    print("Resposta: ", iaChat.text, "\n\n\n")
    print('proxima pergunta', '\n\n')  

