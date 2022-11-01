from time import sleep
import numpy as np
from funções import matriz_onibus, imprime_assento, compra_assento


print('=' * 50)

print(f'      \033[1;30;43mOLÁ, SEJA BEM VINDO A POCOBUS\033[m   ')

print('=' * 50)
# opções cliente
matrizbus = matriz_onibus(7, 4)

while True:
    print('Escolha sua opção')
    menu = int(input('''
        [1] - COMPRAR PASSAGEM.
        [2] - FINALIZAR E GERAR RELATÓRIO
    
    Digite uma opção:  '''))
    # mostrando a matriz do ônibus com os assentos
    if menu != 1 and menu != 2:
        print('\033[1;30;41m Opção Inválida. Por favor, escolha a opção correta.\033[m')
        menu = int(input('''
        [1] - COMPRAR PASSAGEM.
        [2] - FINALIZAR E GERAR RELATÓRIO

    Digite uma opção: \033[m '''))
    elif menu == 1:
        print('Carregando ...')
        sleep(2)
        print('Aqui estão os assentos disponíveis para compra.')
        imprime_assento(matrizbus)
        print('=' * 50)
        print('Prezado Cilente, no momento temos os assentos disponíveis númerados na cor verde.')
        assento = int(input('Digite o número assento desejado: '))
        if assento == 0:
            print('\033[1;30;41m Opção Inválida. Por favor, escolha um assento disponível na cor verde.\033[m')
            assento = int(input('Digite o número assento desejado: '))

# escolhendo os assentos e imprimindo a matriz modificada
        print('Carregando ...')
        sleep(2)
        matrizbus = compra_assento(assento, matrizbus)
        imprime_assento(matrizbus)
        print('-' * 60)
        print(f'Compra Efetuada. Assento número {assento} reservado com sucesso.')
        print('A POCOBUS agradeçe a preferencia e deseja você uma Boa Viagem')
        print('-' * 60)

    else:
        break
compra_assento(matrizbus)
        #imprime_relatorio(matrizbus)


        #with open('Relatório_compra.txt', 'w', encoding='utf-8') as arquivo_compra:
            #arquivo.write(str(matrizbus) + '\n')
# imprimindo o relatório de compra
#print('Carregando ...')

 #   sleep(2)
  #print('Gerando relatório de compra. Aguarde um Momento.')
   #sleep(3)








