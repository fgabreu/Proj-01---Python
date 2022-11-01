import numpy as np
from colorama import Fore, Style

def matriz_onibus(linha, coluna):
    matriz_numpy_inicial = np.arange(1, 29).reshape(linha, coluna)
    linha_superior = [0] * coluna
    linha_central = [0] * (linha + 1)
    matriz_numpy_final = np.insert(matriz_numpy_inicial, 0, [linha_superior], axis=0)
    matriz_numpy_final = np.insert(matriz_numpy_final, 2, [linha_central], axis=1)
    return matriz_numpy_final

def imprime_assento(matrizbus):
    for linha in matrizbus:
        for coluna in linha:
            if coluna > 0:
                print(Style.BRIGHT + Fore.GREEN + f"{coluna:>4}", end=" " + Style.RESET_ALL)
            else:
                print(Style.DIM + Fore.RED + f"{coluna:>4}", end=" " + Style.RESET_ALL)
        print(Style.RESET_ALL)


def compra_assento(assento, matrizbus):
    matriz = np.where(matrizbus == assento, 0, matrizbus)
    return matriz


def cria_relatorio(matriz):
    with open('relatório_compra.txt', 'w', encoding='utf-8') as f:
        for valor in matriz:
            arquivo.write(str(assento) + '\n')
            print(assento)



