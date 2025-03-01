import customtkinter as ctk
from tkinter import *
from window import CadastroWindow
from utils import animate_text


class App(ctk.CTk):
    """Classe principal da aplicação, responsável por criar a janela principal e gerenciar a interface do usuário."""

    # ========== 1. MÉTODO DE INICIALIZAÇÃO ==========
    def __init__(self):
        """Inicializa a aplicação, configurando o layout e a aparência da janela."""
        super().__init__()
        self.layout_config()
        self.appearance()

    # ========== 2. CONFIGURAÇÕES GERAIS ==========
    def layout_config(self):
        """Configura o layout da janela principal, incluindo tamanho, posição e botões."""
        self.title("Sistema de Gestão de Clientes")
        self.center_window(500, 400)

        # Criar botões principais
        self.create_button("Cadastrar", 0.25, self.open_cadastro_window)
        self.create_button("Busca e Edição", 0.4, self.open_search_window)

    def appearance(self):
        """Configura a aparência da janela, incluindo o seletor de tema e o título."""
        self.create_theme_selector()
        self.create_title_label()

    def center_window(self, width, height):
        """Centraliza a janela na tela com base nas dimensões fornecidas."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pos_x = int((screen_width - width) / 2)
        pos_y = int((screen_height - height) / 2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.minsize(width, height)
        self.maxsize(width, height)

    # ========== 3. COMPONENTES DA INTERFACE ==========
    def create_title_label(self):
        """Cria o título da aplicação na janela principal."""
        self.ctk_label = ctk.CTkLabel(
            self, text="Sistema de Gestão de Clientes",
            bg_color="transparent", font=("Arial", 24, "bold")
        )
        self.ctk_label.place(relx=0.5, rely=0.1, anchor="center")
        animate_text(self.ctk_label)

    def create_button(self, text, rely, command):
        """Cria um botão na janela principal."""
        button = ctk.CTkButton(
            self, text=text, command=command,
            width=200, height=50, font=("Arial", 15, "bold")
        )
        button.place(relx=0.5, rely=rely, anchor="center")

    def create_theme_selector(self):
        """Cria o seletor de tema (Dark, Light, System) na janela principal."""
        self.lb_apm = ctk.CTkLabel(
            self, text="Tema",
            bg_color="transparent", text_color=['#000', '#fff'],
            font=("Arial", 13, "bold")
        )
        self.lb_apm.place(relx=0.85, rely=0.89, anchor="center")

        self.opt_apm = ctk.CTkOptionMenu(
            self, values=["Dark", "Light", "System"],
            font=("Arial", 13, "bold"), command=self.change_apm
        )
        self.opt_apm.place(relx=0.85, rely=0.95, anchor="center")

    # ========== 4. FUNCIONALIDADES ==========
    def change_apm(self, nova_aparencia):
        """Altera o tema da aplicação com base na seleção do usuário."""
        ctk.set_appearance_mode(nova_aparencia)

    def open_cadastro_window(self):
        """Abre a janela de cadastro de clientes."""
        CadastroWindow(self)

    def open_search_window(self):
        """Abre a janela de busca e edição de clientes. (Ainda não implementada)"""
        pass

    # ========== 5. ADICIONAR NOVAS FUNÇÕES AQUI ==========
    # Exemplo:
    # def minha_nova_funcao(self):
    #     """Descrição da nova funcionalidade"""
    #     pass


# ========== 6. PONTO DE ENTRADA ==========
if __name__ == "__main__":
    """Cria uma instância da classe App e inicia o loop principal."""
    app = App()
    app.mainloop()
