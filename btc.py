import customtkinter as ctk
from util import limpar_tela
import requests

def abrir_btc(frame_atual, janela):
    from home import abrir_home
    limpar_tela(frame_atual)

    frame = ctk.CTkFrame(frame_atual, fg_color="#BD7B00")
    frame.pack(fill='both', expand=True)

    text = ctk.CTkLabel(frame, text='Cotação atual do Bitcoin', font=('Arial', 20), bg_color="#BD7B00")
    text.place(relx=0.5, rely=0.02, anchor='center')

    price = ctk.CTkLabel(frame_atual, text='', font=('Helvetica', 15), bg_color="#BD7B00")
    price.place(relx=0.5, rely=0.1, anchor='center')

    entry_moeda = ctk.CTkEntry(frame, placeholder_text='Digite seus BTC')
    entry_moeda.place(relx=0.5, rely=0.3, anchor='center')

    ret_moeda = ctk.CTkLabel(frame, text='', font=('helvetica', 12))
    ret_moeda.place(relx=0.5, rely=0.4, anchor='n')

    def pesquisar_btc():
        url = "https://api.coingecko.com/api/v3/simple/price"
        parametros = {'ids': 'bitcoin', 
                      "vs_currencies": 'usd',
        }
        resposta = requests.get(url=url, params=parametros)
        data = resposta.json()

        btc = data.get("bitcoin", {}).get("usd")

        price.configure(text=f'Preço do Bitcoin US$ {btc}$')
        price.after(15000, pesquisar_btc)
        print(f'Valor atual: {btc}')

        def calcular(btc):
            moeda = float(entry_moeda.get())
            res = btc * moeda


            ret_moeda.configure(text=f'Você tem US$ {int(res)} de dolares em BTC')

        if len(entry_moeda.get()) >= 1:
            calcular(btc)

    pesquisar_btc()

    b_voltar = ctk.CTkButton(frame, text='Voltar', command=lambda: abrir_home(frame_atual, janela), width=80)
    b_voltar.place(relx=0.5, rely=0.5, anchor='center')