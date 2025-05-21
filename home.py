import customtkinter as ctk
from util import limpar_tela
from pi import abrir_pi
from btc import abrir_btc

def abrir_home(frame_atual, janela):
    limpar_tela(frame_atual)

    titulo = ctk.CTkLabel(frame_atual, text='Cotação de criptomoedas', font=('Helvetica', 20), text_color="#74FFA2")
    titulo.place(relx=0.5, rely=0.02, anchor='center')

    b_pi = ctk.CTkButton(frame_atual, text='Pi Network', width=80, command=lambda: abrir_pi(frame_atual, janela))
    b_pi.place(relx=0.08, rely=0.3, anchor='center')

    b_btc= ctk.CTkButton(frame_atual, text='Bitcoin', width=80, command=lambda: abrir_btc(frame_atual, janela))
    b_btc.place(relx=0.08, rely=0.4, anchor='center')