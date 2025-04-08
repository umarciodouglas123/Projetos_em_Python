#Márcio Douglas da Silva dos Santos Vieira
#Esse programa cria a tabuada de um número digitado pelo usuário até um número também digitado pelo usuário

import time
import os

#Declaração de variáveis e entrada de dados
a = int(input('Digite qual número deseja a tabuada: \n'))
os.system('cls')
b = int(input('Digite até qual número deseja multiplicar: \n'))
os.system('cls')
c = 0

#Pausa
print('Por favor, aguarde!')
time.sleep(2)
os.system('cls')

#Laço de repetição que calcula e exibe a tabuada
for i in range(b):
    c = i+1
    d = a*c
    print('{}x{}= {}'.format(a,c,d))

print('Obrigado')

#Mantém o CMD aberto até o usuário apertar enter
time.sleep(2)
input('Pressione ENTER para fechar!')