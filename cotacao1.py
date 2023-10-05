import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    # print(texto)

    #pegar_cotacoes()

    texto_cotacao["text"] = texto

janela = Tk()
janela.title("Cotação Atual de Moedas")
janela.geometry("400x200")

texto_orientacao = Label(janela,text = "Clique para carregar a cotação atual")
texto_orientacao.grid(column=1,row=1, padx=10, pady=10)

botao = Button(janela, text="Clique", command=pegar_cotacoes)
botao.grid(column=1, row=2,padx=10, pady=10)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=2, row=4,padx=10, pady=10,)




janela.mainloop()
