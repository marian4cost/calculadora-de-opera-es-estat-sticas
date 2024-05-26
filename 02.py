import tkinter as tk
import statistics
from matplotlib import pyplot as plt 
import pandas as pd

# O PANDAS ERA EXATAMENTE PARA REALIZAR AS OPERAÇÕES E NÃO PARA TÁ INVENTANDO MODA

# VARIÁVEIS GLOBAIS
# tive que puxar as duas variáveis como global se não ia da erro nas funções que iam tentar usar as mesmas variáveis geradas em outra função ;-;
calculo = ""
valorLista = []

# ÁREA PARA FUNÇÕES
# funções de botão
# enviando o tipo de cálculo para o sistema e verificando // da para fazer com a db aqui também 
def enviarTipoCalculo():
    # enviando o dado para o sistema
    global calculo
    calculo = entradaCalculoUsuario.get()
    saidaCalculoUsuario.config(text=f"o cálculo escolhido foi o de {calculo}")

# enviando a lista de valores
def enviarValorLista():
        global valorLista
        valorListaUsuario = entradaValorListaUsuario.get()
        valorLista = valorListaUsuario.split(',')
        valorLista = [int(element.strip())
                      for element in valorLista]
        
        saidaListaUsuario.config(text=f"a lista está assim {valorLista}")

# função para realizar o cálculo
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

# função para geração de gráfico
def gerarGrafico():
        plt.bar(range(len(valorLista)), valorLista, color='b')
        plt.ylabel('valores')
        plt.title(f'operação: {calculo}')
        plt.legend()
        plt.show()

# abrir a janela
janela = tk.Tk()
janela.title("calculadora de operações estatísticas")
janela.geometry("550x250")

# perguntar o tipo de cálculo
textoCalculoUsuario = tk.Label(janela, text="qual o tipo de cálculo que você quer realizar (média, mediana, moda, variância ou desvio padrão):")
textoCalculoUsuario.pack()

entradaCalculoUsuario = tk.Entry(janela, width=75)
entradaCalculoUsuario.pack() 

botaoCalculoUsuario = tk.Button(janela, text="enviar o tipo do cálculo", command=enviarTipoCalculo)
botaoCalculoUsuario.pack()

saidaCalculoUsuario = tk.Label(janela, text="")
saidaCalculoUsuario.pack()

# pedir os valores da lista
textoValorListaUsuario = tk.Label(janela, text="digite a sua lista, separando os elementos com uma vírgula (,)")
textoValorListaUsuario.pack()

entradaValorListaUsuario = tk.Entry(janela, width=25)
entradaValorListaUsuario.pack()

botaoValorListaUsuario = tk.Button(janela, text="enviar lista", command=enviarValorLista)
botaoValorListaUsuario.pack()

saidaListaUsuario = tk.Label(janela, text="")
saidaListaUsuario.pack()

# da o resultado
botaoRealizarCalculo = tk.Button(janela, text="realizar cálculo", command=realizarCalculos)
botaoRealizarCalculo.pack()

saidaResultado = tk.Label(janela, text="")
saidaResultado.pack()

# gerar o gráfico
botaoGerarGrafico = tk.Button(janela, text="gere o gráfico", command=gerarGrafico)
botaoGerarGrafico.pack()

# entregar ao usuário
janela.mainloop()