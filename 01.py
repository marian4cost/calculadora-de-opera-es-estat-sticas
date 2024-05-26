# IMPORTANDO AS BIBLIOTECAS
import pandas as pd
from matplotlib import pyplot as plt
import statistics

df = pd.DataFrame({'media': ['media', 'média', 'Media', 'Média', 'MEDIA', 'MÉDIA'],
                   'mediana': [ 'mediana', 'Mediana', 'MEDIANA', '', '', ''],
                   'moda': [ 'moda', 'Moda', 'MODA', '', '', ''],
                   'variancia': [ 'variancia', 'variância', 'Variancia', 'Variância', 'VARIANCIA', 'VARIÂNCIA'],
                   'desviopadrao': [ 'desviopadrao', 'desviopadrão', 'DesvioPadrao', 'DesvioPadrão', 'DESVIOPADRAO', 'DESVIOPADRÃO']})

tipoCalculo = input('digite o tipo de cálculo que você quer realizar (média, mediana, moda, variância ou desvio padrão):')

ocorrencias = {}
for coluna in df.columns:
    ocorrencias[coluna] = df.index[df[coluna] == tipoCalculo].tolist()

encontrado = False
for coluna, indices in ocorrencias.items():
    if indices:
        encontrado = True
        print(f'{tipoCalculo} é o cálculo de {coluna}')

        if coluna == 'media':
            tipoCalculo = 'media'
        elif coluna == 'mediana':
            tipoCalculo = 'mediana'
        elif coluna == 'moda':
            tipoCalculo = 'moda'
        elif coluna == 'variancia':
            tipoCalculo = 'variancia'
        elif coluna == 'desviopadrao':
            tipoCalculo = 'desviopadrao'

        def selecaoCalculo(coluna, lista):
            if coluna == 'media':
                resultado = statistics.mean(lista)
                print(resultado)
                plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{coluna}: {resultado}')
            elif coluna == 'mediana':
                resultado = statistics.median(lista)
                print(resultado)
                plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{coluna}: {resultado}')
            elif coluna == 'moda':
                resultado = statistics.mode(lista)
                print(resultado)
                plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{coluna}: {resultado}')
            elif coluna == 'variancia':
                resultado = statistics.variance(lista)
                print(resultado)
                plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{coluna}: {resultado}')
            elif coluna == 'desviopadrao':
                resultado = statistics.stdev(lista)
                print(resultado)
                plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{coluna}: {resultado}')

        def criacaoGrafico():
            plt.bar(range(len(lista)), lista, color='g')
            plt.ylabel('valores')
            plt.title(f'operação: {tipoCalculo}')
            plt.legend()
            plt.show()

        lista = []
        def colecaoLista():
            numero = int(input('digite o número desejado para complementar a lista de valores: '))
            lista.append(numero)
            verificacao = input('quer informar um próximo valor (s/n): ')
            while verificacao == 's':
                numero = int(input('digite o número desejado para complementar a lista de valores: '))
                lista.append(numero)
                verificacao = input('quer informar um próximo valor (s/n): ')

if not encontrado:
    print(f'o {tipoCalculo} não ta registrado em nossos bancos')

colecaoLista()
selecaoCalculo(tipoCalculo, lista)
criacaoGrafico()