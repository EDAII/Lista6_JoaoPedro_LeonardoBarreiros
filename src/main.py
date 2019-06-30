from Graph import *
# import pygame
import time
import random
import os.path

def randomForca(): # params: array do grafo que armazena os times
    for forca in range(10):
        forca = random.randint(0, 10) # sorteia habilidade de cada um dos times
    return forca

def geraTimes():
    data = []
    with open('times.txt', 'r') as file:
        objects = file.read().splitlines()
        data.append(objects)
    file.close()
    return data


def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print('1. Classificação de times')
    print('2. Disputa pela taça')
    print('3. Campeão do Brasileirão 2019')
    print("4. Sair")
    print(67 * "-")
# Campeonato de times
# pygame.init()

# display.width = 800
# display.height = 600

# background = (0,0,0)
if __name__ == '__main__':
    carrega = True

times = []

while carrega:
    print_menu()
    opt = input("Selecione opção - [1-4]: ")
    if opt == '1':
        serie = Grafo()
        nomeTime = geraTimes()
        habilidadeTime = randomForca()
        time = Vertice(habilidadeTime, nomeTime)
        for time in times:
            serie.insereVertice(time)
    # elif opt == '2':
    # elif opt == '3':
    elif opt == '4':
        carrega = False
        print('\nSaindo...\n')

    else:
        print('Opção Inválida')