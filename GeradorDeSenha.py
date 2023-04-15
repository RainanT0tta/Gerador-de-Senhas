import string

from random import random, choice

valores = string.ascii_letters 
valores += string.punctuation
valores += string.digits

tamanho = 10
senha = ""


for i in range(tamanho ):
    senha += choice(valores)

print(senha)

