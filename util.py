import sys
import os

def limpar_tela(frame_atual):
    for widget in frame_atual.winfo_children():
        widget.destroy()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)