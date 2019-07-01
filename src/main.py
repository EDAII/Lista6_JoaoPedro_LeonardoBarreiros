from Grafo import *
from Clube import Clube
import random
import time
import json
import os

# instanciar clube - > ler do arquvo e retornar um array de arrays
# instanciar habilidade
# linkar arrays de arrays com cada uma das habilidades
def definirClube():
    with open('times.txt', 'r') as file:
        # i = 0
        #while i < 20:
        lines = file.readlines()
        for data in lines:
            aData = []
            # data = file.readline()[:-1]
            clube = data[:-1], random.randint(0, 10) 
            aData.append(clube)
            # i += 1
            print(aData)

def print_menu():
    print(30 * "-" , "BRASILEIRÃO 2019" , 30 * "-")
    print('1. Classificação de times')
    print('2. Disputa pela taça')
    print('3. Campeão do Brasileirão 2019')
    print("4. Sair")
    print(78 * "-")

if __name__ == '__main__':
    carrega = True

clubes = []

while carrega:
    print_menu()
    opt = input("Selecione opção - [1-4]: ")
    if opt == '1':
        definirClube()    
    # elif opt == '2':
    # elif opt == '3':
    elif opt == '4':
        carrega = False
        print('\nSaindo...\n')

    else:
        print('Opção Inválida')