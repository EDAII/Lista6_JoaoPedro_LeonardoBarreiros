from Grafo import *
import random
import time
import json
import os
import dis

# instanciar clube - > ler do arquvo e retornar um array de arrays
# instanciar habilidade
# linkar arrays de arrays com cada uma das habilidades
def definirClube(aData = []):
    serie = Grafo()
    print(20 * "-", "CLUBES", 20 * "-", "HABILIDADE", 18 * "-")
    with open('times.txt', 'r') as file:
        lines = file.readlines()
        for data in lines:
            dados = data[:-1]
            habilidade = random.randint(0, 10)
            # aData.append({dados:habilidade})
            clube = Vertice()
            clube.nome = dados
            clube.dado = habilidade
            vizinho = Vertice()
            vizinho.nome = dados
            vizinho.dado = habilidade
            # print(clube.nome, clube.dado)
            serie.grafo = {clube.nome:clube.dado}
            # key = hash(serie.grafo)
            print(serie.grafo)
            # serie.insereAresta(key, key)

def print_menu():
    print("\n", 29 * "-" , "BRASILEIRÃO 2019" , 31 * "-")
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
        definirClube(clubes)
    # elif opt == '2':
    # elif opt == '3':
    elif opt == '4':
        carrega = False
        print('\nSaindo...\n')

    else:
        print('Opção Inválida')