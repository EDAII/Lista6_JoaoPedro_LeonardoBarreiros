from Grafo import *
from Clube import Clube
import random
import time
import json
import os

def randomHabilidade():
    habilidade = random.randint(0, 10)
    return habilidade

def getData():
    with open('times.txt', 'r') as file:
        data = file.readline()
    return data

def defineClube(clube):
    nome = getData()
    clube.setNome(nome)

def defineHabilidade(clube):
    habilidade = randomHabilidade()
    clube.setHabilidade(habilidade)

def geraTimes():
    if(os.path.isfile('json_times.txt')):
        file = open('json_times.txt', 'r')
        data_json = file.read()
        data = json.loads(data_json)
        file.close()
    else:
        data = []

    clube = Clube()
    defineClube(clube)
    defineHabilidade(clube)
    file = open('json_times.txt', 'w')
    clube = {"name": clube.getNome(), "Habilidade": clube.getHabilidade()}   
    data.append(clube)
    json_data = json.dumps(data)
    file.writelines(json_data + '\n')
    file.close()

def print_menu():
    print(30 * "-" , "BRASILEIRÃO 2019" , 30 * "-")
    print('1. Classificação de times')
    print('2. Disputa pela taça')
    print('3. Campeão do Brasileirão 2019')
    print("4. Sair")
    print(78 * "-")

if __name__ == '__main__':
    carrega = True

times = []

while carrega:
    print_menu()
    opt = input("Selecione opção - [1-4]: ")
    if opt == '1':
        # serie = Grafo()
        geraTimes()
    # elif opt == '2':
    # elif opt == '3':
    elif opt == '4':
        carrega = False
        print('\nSaindo...\n')

    else:
        print('Opção Inválida')