import customtkinter as ctk
import requests
from util import limpar_tela


def abrir_pi(frame_atual, janela):
    from home import abrir_home
    limpar_tela(frame_atual)
    
    frame = ctk.CTkFrame(frame_atual, fg_color="#9900FF")
    frame.pack(fill='both', expand=True)

    text = ctk.CTkLabel(frame, text='Cotação atual do Pi Network', font=('Arial', 25, 'bold'), bg_color="#9900FF")
    text.place(relx=0.5, rely=0.02, anchor='center')

    price = ctk.CTkLabel(frame, text='', font=('Arial', 20), bg_color='#9900FF')
    price.place(relx=0.5, rely=0.1, anchor='center')

    entry_moeda = ctk.CTkEntry(frame, placeholder_text='Digite seus PI')
    entry_moeda.place(relx=0.5, rely=0.3, anchor='center')

    ret_moeda = ctk.CTkLabel(frame, text='', font=('helvetica', 15))
    ret_moeda.place(relx=0.5, rely=0.4, anchor='n')

    def pesquisar_pi():
        url = "https://api.coingecko.com/api/v3/simple/price"
        parametros = {'ids': 'pi-network', 
                      "vs_currencies": 'usd',
        }
        resposta = requests.get(url=url, params=parametros)
        data = resposta.json()

        pi = data.get("pi-network", {}).get("usd")

        if pi == None:
            price.configure(text=f'Preço do Pi Network não esta disponivel no momento')
            price.after(15000, pesquisar_pi)
            print(f'Valor atual: não disponivel no momento')
        else:    
            price.configure(text=f'Preço do Pi Network US$ {pi}')
            price.after(15000, pesquisar_pi)
            print(f'Valor atual: {pi}')

        
        def calcular(pi):

            if pi != None:
                moeda = float(entry_moeda.get())
                res = pi * moeda
                ret_moeda.configure(text=f'Você tem US$ {int(res)} de dolares em PI')
            else:
                ret_moeda.configure(text=f'Preço do Pi Network não disponivel no momento... Aguarde!')

        if len(entry_moeda.get()) >= 1:
            calcular(pi)

    pesquisar_pi()

    b_voltar = ctk.CTkButton(frame, text='Voltar', command=lambda: abrir_home(frame_atual, janela), width=80, bg_color="#9900FF")
    b_voltar.place(relx=0.5, rely=0.5, anchor='center')

