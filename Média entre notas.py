#Márcio Douglas da Silva dos Santos Vieira
#Esse programa calcula a média entre n notas e retorna se o aluno está aprovado ou não baseado em uma nota de corte

import time

#Declaração de variáveis e entrada de dados
n = int(input('Quantas notas são?\n'))
c = float(input('Qual a nota de corte?\n'))
pf = 0

#Iniciando o somatório das notas
soma = 0

#Estrutura de repetição com alcance em n para adicionar as notas e somá-las
for i in range(n):
    nota = float(input(f'Digite a {i+1}ª nota:\n'))
    soma = soma + nota

#Cálculo da média
media = soma / n

#Exibindo na tela a média
print('A média das notas desse aluno é: {:.2f}'.format(media))

#Pausa
print('Por favor, aguarde!')
time.sleep(2)

#Estrutura condicional para dar significado às notas
if media < c:
    print('Aluno precisrá fazer uma prova final!')
    pf = 10 - media
    print('Por gentileza, aguarde!')
    time.sleep(2)
    print('Nessa prova final o aluno precisará de {:.2f} pontos para ser aprovado'.format(pf))
if media == c:
    print('Entre em contato com o aluno e pergunte se ele deseja fazer a prova final. Em caso de recusa, ele estará aprovado!')
if media > c:
    print('Aluno aprovado!')

#Agradecimentos
time.sleep(2)
print('Obrigado!')

#Mantém o CMD aberto até o usuário apertar enter
time.sleep(2)
input('Pressione ENTER para fechar!')