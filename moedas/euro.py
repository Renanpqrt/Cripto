import customtkinter as ctk
import requests
from util import limpar_tela

def abrir_euro(frame_atual, janela):
    from home import abrir_home
    limpar_tela(frame_atual)

    euro = None

    frame = ctk.CTkFrame(frame_atual, fg_color="#746303")
    frame.pack(fill='both', expand=True)

    titulo = ctk.CTkLabel(frame, text='Cotação atual do Euro', font=('Arial', 25, 'bold'))
    titulo.place(relx=0.5, rely=0.02, anchor='center')

    b_voltar = ctk.CTkButton(frame, text='Voltar', command=lambda: abrir_home(frame_atual, janela), width=80, bg_color="#746303")
    b_voltar.place(relx=0.5, rely=0.6, anchor='center')

    price = ctk.CTkLabel(frame, text='', font=('Arial', 20), bg_color='#746303')
    price.place(relx=0.5, rely=0.1, anchor='center')

    entry_eur = ctk.CTkEntry(frame, placeholder_text='Euros')
    entry_eur.place(relx=0.5, rely=0.3, anchor='center')

    ret = ctk.CTkLabel(frame, text='', font=('Helvetica', 15))
    ret.place(relx=0.5, rely=0.5, anchor='center')


    def pesquisar_dolar():
        url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
        global euro

        resposta = requests.get(url)
        data = resposta.json()

        euro = data.get('EURBRL', {}).get('bid')
        if euro == None:
            price.configure(text='O preço do euro atualmente não esta disponivel no momento')
        else:    
            price.configure(text=f'O preço do euro atualmente esta em R${euro}')

    def calcular():
        global euro

        if euro != None:
            eur = float(entry_eur.get())
            res = eur * float(euro)
            ret.configure(text=f'Seus euros convertidos para reais são iguais a R${int(res)}')
        else:
            ret.configure(text='Preço do euro não disponivel no momento... Aguarde!')
        
    b_calcular = ctk.CTkButton(frame, text='Calcular', width=80, command=calcular)
    b_calcular.place(relx=0.5, rely=0.4, anchor='center')


    pesquisar_dolar()