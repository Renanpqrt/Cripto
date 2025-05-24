import customtkinter as ctk
from util import limpar_tela
from Criptomoedas.pi import abrir_pi
from Criptomoedas.btc import abrir_btc
from moedas.dolar import abrir_dolar
from moedas.euro import abrir_euro
from PIL import Image
from customtkinter import CTkImage

def abrir_home(frame_atual, janela):
    limpar_tela(frame_atual)

    titulo = ctk.CTkLabel(frame_atual, text='Cotação das criptomoedas/moedas', font=('Helvetica', 25, 'bold'), text_color="#74FFA2")
    titulo.place(relx=0.5, rely=0.02, anchor='center')

    b_pi = ctk.CTkButton(frame_atual, text='Pi Network', width=80, command=lambda: abrir_pi(frame_atual, janela), corner_radius=12)
    b_pi.place(relx=0.08, rely=0.3, anchor='center')

    b_btc= ctk.CTkButton(frame_atual, text='Bitcoin', width=80, command=lambda: abrir_btc(frame_atual, janela), corner_radius=12)
    b_btc.place(relx=0.08, rely=0.4, anchor='center')

    b_dolar = ctk.CTkButton(frame_atual, text='Dolar', width=80, command=lambda: abrir_dolar(frame_atual, janela), corner_radius=12)
    b_dolar.place(relx=0.92, rely=0.3, anchor='center')

    b_euro = ctk.CTkButton(frame_atual, text='Euro', width=80, command=lambda: abrir_euro(frame_atual, janela), corner_radius=12)
    b_euro.place(relx=0.92, rely=0.4, anchor='center')