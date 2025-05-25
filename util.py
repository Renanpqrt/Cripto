def limpar_tela(frame_atual):
    for widget in frame_atual.winfo_children():
        widget.destroy()

