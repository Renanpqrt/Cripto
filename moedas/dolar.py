import customtkinter as ctk
import requests
from util import limpar_tela

def abrir_dolar(frame_atual, janela):
    from home import abrir_home
    limpar_tela(frame_atual)

    dolar = None

    frame = ctk.CTkFrame(frame_atual, fg_color="#28881F")
    frame.pack(fill='both', expand=True)

    titulo = ctk.CTkLabel(frame, text='Cotação atual do Dolar', font=('Arial', 25, 'bold'))
    titulo.place(relx=0.5, rely=0.02, anchor='center')

    b_voltar = ctk.CTkButton(frame, text='Voltar', command=lambda: abrir_home(frame_atual, janela), width=80, bg_color="#28881F")
    b_voltar.place(relx=0.5, rely=0.6, anchor='center')

    price = ctk.CTkLabel(frame, text='', font=('Arial', 20), bg_color='#28881F')
    price.place(relx=0.5, rely=0.1, anchor='center')

    entry_doll = ctk.CTkEntry(frame, placeholder_text='Dolares')
    entry_doll.place(relx=0.5, rely=0.3, anchor='center')

    ret = ctk.CTkLabel(frame, text='', font=('Helvetica', 15))
    ret.place(relx=0.5, rely=0.5, anchor='center')


    def pesquisar_dolar():
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        global dolar

        resposta = requests.get(url)
        data = resposta.json()

        dolar = data.get('USDBRL', {}).get('bid')
        if dolar == None:
            price.configure(text='O preço do dolar atualmente não esta disponivel no momento')
        else:    
            price.configure(text=f'O preço do dolar atualmente esta em R${dolar}')

    def calcular():
        global dolar

        if dolar != None:
            doll = float(entry_doll.get())
            res = doll * float(dolar)
            ret.configure(text=f'Seus dolares convertidos para reais são iguais a R${int(res)}')
        else:
            ret.configure(text='Preço do dolar não disponivel no momento... Aguarde!')
        
    b_calcular = ctk.CTkButton(frame, text='Calcular', width=80, command=calcular)
    b_calcular.place(relx=0.5, rely=0.4, anchor='center')


    pesquisar_dolar()