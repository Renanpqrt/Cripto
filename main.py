import customtkinter as ctk
from home import abrir_home

def iniciar():
    app = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app.geometry('600x600')
    app.title('Cotações')
    app.resizable(False, False)

    frame_principal = ctk.CTkFrame(app, fg_color="#082449")
    frame_principal.pack(fill="both", expand=True)

    abrir_home(frame_principal, app)

    app.mainloop()

iniciar()
