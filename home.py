import customtkinter as ctk
from util import limpar_tela, resource_path
from Criptomoedas.pi import abrir_pi
from Criptomoedas.btc import abrir_btc
from moedas.dolar import abrir_dolar
from moedas.euro import abrir_euro
from PIL import Image
from customtkinter import CTkImage

def abrir_home(frame_atual, janela):
    limpar_tela(frame_atual)

    fundo_img = Image.open(resource_path("imagens/fundo.png"))
    fundo_img = CTkImage(light_image=fundo_img, size=(600, 600))

    fundo = ctk.CTkLabel(frame_atual, image=fundo_img, text='')
    fundo.place(relx=0.5, rely=0.5, anchor='center')

    titulo = ctk.CTkLabel(frame_atual, text='Cotações', font=('Helvetica', 25, 'bold'), text_color="#ffffff", bg_color='#00d147')
    titulo.place(relx=0.5, rely=0.02, anchor='center')

    pi_img = Image.open(resource_path("imagens/pi.png"))
    pi_img = CTkImage(light_image=pi_img, size=(30, 30))

    b_pi = ctk.CTkButton(frame_atual, text='', image=pi_img, width=80, command=lambda: abrir_pi(frame_atual, janela), bg_color='#05bf44', fg_color='#05bf44', hover_color='#05bf44')
    b_pi.place(relx=0.08, rely=0.3, anchor='center')

    btc_img = Image.open(resource_path("imagens/bitcoin.png"))
    btc_img = CTkImage(light_image=btc_img, size=(30, 30))

    b_btc= ctk.CTkButton(frame_atual, text='', image=btc_img, width=80, command=lambda: abrir_btc(frame_atual, janela), bg_color='#05bf44', fg_color='#05bf44', hover_color='#05bf44')
    b_btc.place(relx=0.08, rely=0.4, anchor='center')

    dolar_img = Image.open(resource_path("imagens/dolar.png"))
    dolar_img = CTkImage(light_image=dolar_img, size=(30, 30))

    b_dolar = ctk.CTkButton(frame_atual, text='', image=dolar_img, width=80, command=lambda: abrir_dolar(frame_atual, janela), bg_color='#00d147', fg_color="#00d147", hover_color="#00d147")
    b_dolar.place(relx=0.92, rely=0.3, anchor='center')

    euro_img = Image.open(resource_path("imagens/euro.png"))
    euro_img = CTkImage(light_image=euro_img, size=(30, 30))

    b_euro = ctk.CTkButton(frame_atual, text='', image=euro_img, width=80, command=lambda: abrir_euro(frame_atual, janela), bg_color='#00d147', fg_color="#00d147", hover_color="#00d147")
    b_euro.place(relx=0.92, rely=0.4, anchor='center')