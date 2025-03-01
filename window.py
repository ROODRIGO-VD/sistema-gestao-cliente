import customtkinter as ctk
from tkinter import filedialog
from validate_docbr import CPF
from utils import animate_text
from PIL import Image, ImageTk


class CadastroWindow:
    """Classe responsável por criar e gerenciar a janela de cadastro de clientes."""

    # ========== 1. MÉTODO DE INICIALIZAÇÃO ==========
    def __init__(self, parent):
        """Inicializa a janela de cadastro, configurando layout e campos de entrada."""
        self.new_window = ctk.CTkToplevel(parent)
        self.new_window.geometry("800x600")
        self.new_window.minsize(800, 600)
        self.new_window.maxsize(800, 600)
        self.new_window.title("Cadastro de Cliente")

        # Garante que a nova janela apareça na frente da principal
        self.new_window.transient(parent)
        self.new_window.grab_set()

        self.center_window()
        self.create_widgets()

    # ========== 2. MÉTODOS DE CONFIGURAÇÃO ==========
    def center_window(self):
        """Centraliza a janela na tela."""
        screen_width = self.new_window.winfo_screenwidth()
        screen_height = self.new_window.winfo_screenheight()
        pos_x = int((screen_width - 800) / 2)
        pos_y = int((screen_height - 600) / 2)
        self.new_window.geometry(f"800x600+{pos_x}+{pos_y}")

    def create_widgets(self):
        """Cria todos os elementos da interface gráfica."""
        self.create_title_label()
        self.create_foto_section()
        self.create_name_field()
        self.create_cpf_field()

    # ========== 3. COMPONENTES DA INTERFACE ==========
    def create_title_label(self):
        """Cria o título da janela de cadastro."""
        self.ctk_label = ctk.CTkLabel(
            self.new_window,
            text="Cadastro de Cliente",
            font=("Arial", 24, "bold"),
            fg_color="transparent",
            text_color=("#2B6FB6", "#3B8ED0"),
            corner_radius=10
        )
        self.ctk_label.place(relx=0.5, rely=0.05, anchor="center")
        animate_text(self.ctk_label)

    def create_foto_section(self):
        """Cria a seção para exibição da foto com borda fixa e botões."""
        self.canvas = ctk.CTkCanvas(
            self.new_window, width=162, height=162, bg="white", highlightthickness=0)
        self.canvas.place(x=20, y=70)
        self.canvas.create_rectangle(1, 1, 161, 161, outline="gray", width=2)

        self.foto_label = ctk.CTkLabel(
            self.new_window, text="", width=160, height=160, fg_color="transparent")
        self.foto_label.place(x=21, y=71)

        self.btn_selecionar_foto = ctk.CTkButton(
            self.new_window, text="Selecionar Foto", width=120, height=32, command=self.selecionar_foto, font=("Arial", 13, "bold")
        )
        self.btn_selecionar_foto.place(x=36, y=238)

        self.btn_apagar_foto = ctk.CTkButton(
            self.new_window, text="Apagar Foto", width=120, height=32, command=self.apagar_foto, font=("Arial", 13, "bold")
        )
        self.btn_apagar_foto.place(x=36, y=288)

    def create_name_field(self):
        """Cria o campo de entrada para o nome do cliente."""
        self.name_label = ctk.CTkLabel(
            self.new_window, text="Nome", font=("Arial", 14, "bold"))
        self.name_label.place(x=190, y=80)

        def validate_input(text):
            return all(char.isalpha() or char.isspace() for char in text)

        def validate_length(text):
            return len(text) <= 100

        def combine_validations(text):
            return validate_length(text) and validate_input(text)

        vcmd = (self.new_window.register(combine_validations), '%P')

        self.name_entry = ctk.CTkEntry(
            self.new_window, width=250, height=35, validate="key", validatecommand=vcmd)
        self.name_entry.place(x=190, y=110)
        self.name_entry.bind("<FocusOut>", self.format_name_entry)

    def create_cpf_field(self):
        """Cria o campo de entrada para o CPF do cliente."""
        self.cpf_label = ctk.CTkLabel(
            self.new_window, text="CPF", font=("Arial", 14, "bold"))
        self.cpf_label.place(x=190, y=150)

        def validate_cpf_input(number):
            return number.isdigit()

        def validate_cpf_length(number):
            return len(number) <= 11

        def combine_cpf_validations(number):
            return number == "" or (validate_cpf_length(number) and validate_cpf_input(number))

        vcmd_cpf = (self.new_window.register(combine_cpf_validations), '%P')

        self.cpf_entry = ctk.CTkEntry(
            self.new_window, width=250, height=35, validate="key", validatecommand=vcmd_cpf)
        self.cpf_entry.place(x=190, y=180)

        self.cpf_validation_label = ctk.CTkLabel(
            self.new_window, text="", font=("Arial", 13))
        self.cpf_validation_label.place(x=440, y=180)

        self.cpf_entry.bind("<KeyRelease>", self.validate_cpf)
        self.cpf_entry.bind("<FocusOut>", self.format_cpf_entry)

    # ========== 4. FUNCIONALIDADES ==========
    def selecionar_foto(self):
        """Abre o seletor de arquivos e carrega a imagem escolhida dentro da borda."""
        caminho_imagem = filedialog.askopenfilename(
            title="Selecionar Imagem",
            filetypes=[("Imagens", "*.png;*.jpg;*.jpeg"),
                       ("Todos os arquivos", "*.*")]
        )
        if caminho_imagem:
            imagem = Image.open(caminho_imagem).convert("RGBA")
            imagem = imagem.resize((160, 160), Image.Resampling.LANCZOS)

            imagem_tk = ImageTk.PhotoImage(imagem)
            self.foto_label.configure(image=imagem_tk)
            self.foto_label.image = imagem_tk  # Mantém a referência

    def apagar_foto(self):
        """Remove a imagem exibida, mantendo a borda fixa."""
        self.foto_label.configure(image="")
        self.foto_label.image = None  # Remove a referência da imagem

    def validate_cpf(self, event=None):
        """Verifica se o CPF é válido e exibe um ícone de confirmação."""
        cpf = self.cpf_entry.get().strip()
        if CPF().validate(cpf):
            self.cpf_validation_label.configure(text="✔️", text_color="green")
        else:
            self.cpf_validation_label.configure(text="❌", text_color="red")

    def format_name_entry(self, event=None):
        """Formata o nome (remove espaços extras e capitaliza palavras)."""
        text = self.name_entry.get().strip().title()
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, text)

    def format_cpf_entry(self, event=None):
        """Remove espaços extras do CPF."""
        text = self.cpf_entry.get().strip()
        self.cpf_entry.delete(0, "end")
        self.cpf_entry.insert(0, text)

    # ========== 5. ADICIONAR NOVAS FUNÇÕES AQUI ==========
    # Exemplo:
    # def minha_nova_funcao(self):
    #     """Descrição da nova funcionalidade"""
    #     pass
