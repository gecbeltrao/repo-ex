import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

# =========================
# JANELA PRINCIPAL
# =========================

janela = tk.Tk()
janela.title("Sistema Escolar")
janela.geometry("1100x650")
janela.config(bg="#dcdcdc")

# =========================
# CONEXÃO MYSQL
# =========================

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="gecbeltrao",
        password="Yron@1987",
        database="escola_2"
    )

    cursor = conn.cursor()

    if conn.is_connected():
        print("Conexão realizada com sucesso!")

except mysql.connector.Error as error:
    print("Falha na conexão!", error)

# =========================
# FUNÇÕES AUXILIARES
# =========================

def limpar_frame():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

# =========================
# MENU LATERAL
# =========================

frame_menu = tk.Frame(janela, bg="#6d96e8", width=220)
frame_menu.pack(side="left", fill="y")

# =========================
# LOGO
# =========================

logo = Image.open(r"C:\Users\gecbe\Documents\teste\SchoolSyst.png")
logo = logo.resize((200, 200))

logo_tk = ImageTk.PhotoImage(logo)

label_logo = tk.Label(
    frame_menu,
    image=logo_tk,
    bg="#6d96e8"
)

label_logo.pack(pady=20)

# =========================
# ÁREA DE CONTEÚDO
# =========================

frame_conteudo = tk.Frame(
    janela,
    bg="#e5e5e5"
)

frame_conteudo.pack(
    side="right",
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# =========================
# ESTILO DOS BOTÕES
# =========================

def criar_botao(texto, comando):
    return tk.Button(
        frame_menu,
        text=texto,
        command=comando,
        width=18,
        height=2,
        bg="#87aef5",
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        cursor="hand2"
    )

# =========================
# CADASTRAR ALUNO
# =========================

def cadastrar():

    limpar_frame()

    titulo = tk.Label(
        frame_conteudo,
        text="Cadastrar aluno",
        font=("Arial", 24, "bold"),
        bg="#e5e5e5"
    )
    titulo.pack(pady=20)

    tk.Label(
        frame_conteudo,
        text="Nome do aluno:",
        font=("Arial", 14),
        bg="#e5e5e5"
    ).pack()

    entry_nome = tk.Entry(
        frame_conteudo,
        font=("Arial", 14),
        width=30
    )
    entry_nome.pack(pady=10)

    def salvar():

        nome = entry_nome.get()

        if nome == "":
            messagebox.showerror("Erro", "Digite um nome")
            return

        cursor.execute(
            "INSERT INTO alunos(nome) VALUES (%s)",
            (nome,)
        )

        conn.commit()

        messagebox.showinfo(
            "Sucesso",
            "Aluno cadastrado!"
        )

        entry_nome.delete(0, tk.END)

    tk.Button(
        frame_conteudo,
        text="Salvar",
        command=salvar,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=15,
        relief="flat"
    ).pack(pady=20)

# =========================
# CADASTRAR NOTAS
# =========================

def cadastrarnotas():

    limpar_frame()

    titulo = tk.Label(
        frame_conteudo,
        text="Cadastrar notas",
        font=("Arial", 24, "bold"),
        bg="#e5e5e5"
    )
    titulo.pack(pady=20)

    labels = [
        "Primeira nota",
        "Segunda nota",
        "ID do aluno"
    ]

    entradas = []

    for texto in labels:

        tk.Label(
            frame_conteudo,
            text=texto,
            font=("Arial", 14),
            bg="#e5e5e5"
        ).pack()

        entry = tk.Entry(
            frame_conteudo,
            font=("Arial", 14),
            width=20
        )

        entry.pack(pady=8)

        entradas.append(entry)

    def salvar():

        nota1 = entradas[0].get()
        nota2 = entradas[1].get()
        id_aluno = entradas[2].get()

        cursor.execute(
            """
            INSERT INTO notas(nota1, nota2, id_aluno)
            VALUES (%s,%s,%s)
            """,
            (nota1, nota2, id_aluno)
        )

        conn.commit()

        messagebox.showinfo(
            "Sucesso",
            "Notas cadastradas!"
        )

        for entry in entradas:
            entry.delete(0, tk.END)

    tk.Button(
        frame_conteudo,
        text="Salvar",
        command=salvar,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=15,
        relief="flat"
    ).pack(pady=20)

# =========================
# LISTAR ALUNOS
# =========================

def listar_aluno():

    limpar_frame()

    titulo = tk.Label(
        frame_conteudo,
        text="Lista de alunos",
        font=("Arial", 24, "bold"),
        bg="#e5e5e5"
    )
    titulo.pack(pady=20)

    lista = tk.Listbox(
        frame_conteudo,
        font=("Arial", 14),
        width=50,
        height=15
    )

    lista.pack(pady=10)

    cursor.execute("SELECT * FROM alunos")

    for aluno in cursor.fetchall():
        lista.insert(
            tk.END,
            f"ID: {aluno[0]}   |   Nome: {aluno[1]}"
        )

# =========================
# TABELA
# =========================

def listar_tabela():

    limpar_frame()

    titulo = tk.Label(
        frame_conteudo,
        text="Tabela de alunos",
        font=("Arial", 24, "bold"),
        bg="#e5e5e5"
    )

    titulo.pack(pady=20)

    estilo = ttk.Style()

    estilo.theme_use("default")

    estilo.configure(
        "Treeview",
        background="white",
        foreground="black",
        rowheight=35,
        fieldbackground="white",
        font=("Arial", 12)
    )

    estilo.configure(
        "Treeview.Heading",
        font=("Arial", 13, "bold"),
        background="#87aef5",
        foreground="black"
    )

    tabela = ttk.Treeview(
        frame_conteudo,
        columns=("id", "nome", "nota1", "nota2"),
        show="headings",
        height=15
    )

    tabela.heading("id", text="ID")
    tabela.heading("nome", text="NOME")
    tabela.heading("nota1", text="NOTA 1")
    tabela.heading("nota2", text="NOTA 2")

    tabela.column("id", width=80, anchor="center")
    tabela.column("nome", width=300, anchor="center")
    tabela.column("nota1", width=150, anchor="center")
    tabela.column("nota2", width=150, anchor="center")

    tabela.pack(fill="both", expand=True)

    cursor.execute("""
        SELECT alunos.id,
               alunos.nome,
               notas.nota1,
               notas.nota2
        FROM alunos
        LEFT JOIN notas
        ON alunos.id = notas.id_aluno
    """)

    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)

# =========================
# EXCLUIR TUDO
# =========================

def excluir_tudo():

    resposta = messagebox.askyesno(
        "Confirmação",
        "Deseja excluir tudo?"
    )

    if resposta:

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("DELETE FROM alunos")
        cursor.execute("DELETE FROM notas")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        conn.commit()

        messagebox.showinfo(
            "Sucesso",
            "Dados excluídos!"
        )

# =========================
# ATUALIZAR NOME
# =========================

def atualizar_nome():

    limpar_frame()

    titulo = tk.Label(
        frame_conteudo,
        text="Atualizar nome",
        font=("Arial", 24, "bold"),
        bg="#e5e5e5"
    )

    titulo.pack(pady=20)

    tk.Label(
        frame_conteudo,
        text="ID do aluno",
        font=("Arial", 14),
        bg="#e5e5e5"
    ).pack()

    entry_id = tk.Entry(
        frame_conteudo,
        font=("Arial", 14)
    )

    entry_id.pack(pady=10)

    tk.Label(
        frame_conteudo,
        text="Novo nome",
        font=("Arial", 14),
        bg="#e5e5e5"
    ).pack()

    entry_nome = tk.Entry(
        frame_conteudo,
        font=("Arial", 14)
    )

    entry_nome.pack(pady=10)

    def atualizar():

        try:
            aluno_id = int(entry_id.get())

        except:
            messagebox.showerror(
                "Erro",
                "ID inválido"
            )
            return

        novo_nome = entry_nome.get()

        cursor.execute(
            "SELECT id FROM alunos WHERE id = %s",
            (aluno_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:

            messagebox.showerror(
                "Erro",
                "Aluno não encontrado"
            )

            return

        cursor.execute(
            """
            UPDATE alunos
            SET nome = %s
            WHERE id = %s
            """,
            (novo_nome, aluno_id)
        )

        conn.commit()

        messagebox.showinfo(
            "Sucesso",
            "Nome atualizado!"
        )

    tk.Button(
        frame_conteudo,
        text="Atualizar",
        command=atualizar,
        bg="#ff9800",
        fg="white",
        font=("Arial", 12, "bold"),
        width=15,
        relief="flat"
    ).pack(pady=20)

# =========================
# BOTÕES MENU
# =========================

criar_botao("Cadastrar aluno", cadastrar).pack(pady=10)

criar_botao("Cadastrar notas", cadastrarnotas).pack(pady=10)

criar_botao("Listar alunos", listar_aluno).pack(pady=10)

criar_botao("Listar tudo", listar_tabela).pack(pady=10)

criar_botao("Atualizar nome", atualizar_nome).pack(pady=10)

tk.Button(
    frame_menu,
    text="Excluir tudo",
    command=excluir_tudo,
    width=18,
    height=2,
    bg="#e53935",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
).pack(pady=30)

# =========================
# LOOP
# =========================

janela.mainloop()