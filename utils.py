import customtkinter as ctk


def animate_text(label):
    """
    Alterna a cor do texto do label entre preto e vermelho.

    Args:
        label (ctk.CTkLabel): O label cujo texto será animado.
    """
    current_color = label.cget("text_color")
    new_color = "blue" if current_color == "white" else "white"
    label.configure(text_color=new_color)
    label.after(500, animate_text, label)  # Agenda a próxima chamada da função
