# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#  Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima? Responda com sim ou não: ",
    "Esteve no local do crime? Responda com sim ou não: ",
    "Mora perto da vítima? Responda com sim ou não: ",
    "Devia para a vítima? Responda com sim ou não: ",
    "Já trabalhou com a vítima? Responda com sim ou não: "]

sim = 0

for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()  
    if resposta == "sim":  
        sim += 1  

if sim == 2:
    classificacao = "Suspeita"
elif 3 <= sim <= 4:
    classificacao = "Cúmplice"
elif sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"Classificação: {classificacao}")