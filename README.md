# Gerador-de-Senhas
Este é um gerador de senhas simples e eficiente, desenvolvido em Python. Com este programa, você pode gerar senhas fortes e aleatórias em questão de segundos.
O usuário pode escolher o comprimento da senha e quais caracteres devem ser usados, como letras maiúsculas e minúsculas, números e símbolos. 
 As senhas geradas são seguras e podem ser usadas para contas online, como e-mails, redes sociais, bancos e outras. Além disso, o programa não armazena as senhas geradas, o que garante ainda mais segurança para o usuário. 
 Com este gerador de senhas, você pode ficar tranquilo sabendo que suas contas online estão protegidas por senhas fortes e seguras.
 
 
 
 
 
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
