'''

Crie um programa onde o usuário decide qual equação ele deseja calcular: equação do 1º grau ou equação do 2º grau.

'''

#Importando um biblioteca para usar a função SQRT (math.sqrt{valor})

import math

def exibir_menu():
    print(f'{'*'*30} CALCULADORA DE EQUAÇÕES {'*'*30}\n')

    print('Digite 1: para equação de 1º grau.')
    print('Digite 2: para equação de 2º grau.\n')

def equacao_1 (a, b):
    calculo = -b / a
    return calculo

def equacao_2 (a, b,c):
    calculo = a + b + c
    return calculo

#Programa principal
while True:

    exibir_menu()
    opcao = int(input('Informe a opção desejada: '))
    print('')

    if opcao == 1:
        print('Equação de 1º grau: ax+ b = 0\n')
        a = float(input('Informe o primeiro número: '))
        b = float(input('Informe o segundo número: '))
        resultado = equacao_1(a,b)
        print(f' O resultado da equação de 1º grau é {resultado}.')
    elif opcao == 2:
        print('Equação de 2º grau: ax² + bx + c = 0\n')
        a = float(input('Informe o primeiro número: '))
        b = float(input('Informe o segundo número: '))
        c = float(input('Informe o terceiro número: '))
        resultado = equacao_2(a,b,c)
        print(f'O resultado da equação de 2º grau é {resultado}.\n')
    else:
        break