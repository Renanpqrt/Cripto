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

    b_pi = ctk.CTkButton(frame_atual, text='Pi Network', width=80, command=lambda: abrir_pi(frame_atual, janela), corner_radius=12, bg_color='#05bf44')
    b_pi.place(relx=0.08, rely=0.3, anchor='center')

    b_btc= ctk.CTkButton(frame_atual, text='Bitcoin', width=80, command=lambda: abrir_btc(frame_atual, janela), corner_radius=12, bg_color='#05bf44')
    b_btc.place(relx=0.08, rely=0.4, anchor='center')

    b_dolar = ctk.CTkButton(frame_atual, text='Dolar', width=80, command=lambda: abrir_dolar(frame_atual, janela), corner_radius=12, bg_color='#00d147')
    b_dolar.place(relx=0.92, rely=0.3, anchor='center')

    b_euro = ctk.CTkButton(frame_atual, text='Euro', width=80, command=lambda: abrir_euro(frame_atual, janela), corner_radius=12, bg_color='#00d147')
    b_euro.place(relx=0.92, rely=0.4, anchor='center')