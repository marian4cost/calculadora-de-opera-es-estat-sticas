import tkinter as tk
from matplotlib import pyplot as plt 
import pandas as pd

calculo = ""
valorLista = []

def enviarTipoCalculo():
    # enviando o dado para o sistema
    global calculo
    calculo = entradaCalculoUsuario.get()
    saidaCalculoUsuario.config(text=f"o cálculo escolhido foi o de {calculo}")

def enviarValorLista():
        global valorLista
        valorListaUsuario = entradaValorListaUsuario.get()
        valorLista = valorListaUsuario.split(',')
        valorLista = [int(element.strip())
                      for element in valorLista]
        
        saidaListaUsuario.config(text=f"a lista está assim {valorLista}")

def realizarCalculos():
    seriesValorLista = pd.Series(valorLista)
    if calculo == "media":
        resultado = seriesValorLista.mean()
        saidaResultado.config(text=f"o resultado do cálculo de {calculo} é {resultado}")

        plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{calculo}: {resultado}')
    elif calculo == "mediana":
        resultado = seriesValorLista.median()
        saidaResultado.config(text=f"o resultado do cálculo de {calculo} é {resultado}")

        plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{calculo}: {resultado}')
    elif calculo == "moda":
        resultado = seriesValorLista.mode()
        saidaResultado.config(text=f"o resultado do cálculo de {calculo} é {resultado}")

        plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{calculo}: {resultado}')
    elif calculo == "variancia":
        resultado = seriesValorLista.var
        saidaResultado.config(text=f"o resultado do cálculo de {calculo} é {resultado}")

        plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{calculo}: {resultado}')
    elif calculo == "desvioPadrao":
        resultado = seriesValorLista.std()
        saidaResultado.config(text=f"o resultado do cálculo de {calculo} é {resultado}")

        plt.axhline(resultado, color='r', linestyle='--', linewidth=2, label=f'{calculo}: {resultado}')
    else:
        saidaCalculoUsuario.config(text="informe um valor valido")

def gerarGrafico():
        plt.bar(range(len(valorLista)), valorLista, color='b')
        plt.ylabel('valores')
        plt.title(f'operação: {calculo}')
        plt.legend()
        plt.show()

janela = tk.Tk()
janela.title("calculadora de operações estatísticas")
janela.geometry("550x250")

textoCalculoUsuario = tk.Label(janela, text="qual o tipo de cálculo que você quer realizar (média, mediana, moda, variância ou desvio padrão):")
textoCalculoUsuario.pack()
entradaCalculoUsuario = tk.Entry(janela, width=75)
entradaCalculoUsuario.pack() 
botaoCalculoUsuario = tk.Button(janela, text="enviar o tipo do cálculo", command=enviarTipoCalculo)
botaoCalculoUsuario.pack()
saidaCalculoUsuario = tk.Label(janela, text="")
saidaCalculoUsuario.pack()

textoValorListaUsuario = tk.Label(janela, text="digite a sua lista, separando os elementos com uma vírgula (,)")
textoValorListaUsuario.pack()
entradaValorListaUsuario = tk.Entry(janela, width=25)
entradaValorListaUsuario.pack()
botaoValorListaUsuario = tk.Button(janela, text="enviar lista", command=enviarValorLista)
botaoValorListaUsuario.pack()
saidaListaUsuario = tk.Label(janela, text="")
saidaListaUsuario.pack()

botaoRealizarCalculo = tk.Button(janela, text="realizar cálculo", command=realizarCalculos)
botaoRealizarCalculo.pack()
saidaResultado = tk.Label(janela, text="")
saidaResultado.pack()

botaoGerarGrafico = tk.Button(janela, text="gere o gráfico", command=gerarGrafico)
botaoGerarGrafico.pack()

janela.mainloop()