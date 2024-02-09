import tkinter as tk
from tkinter import messagebox

# Funções CRUD
def buscar_informacoes_aluno(nome_aluno):
    try:
        with open("alunos.txt", "r") as file:
            for linha in file:
                nome, serie, email, senha = linha.strip().split(',')
                if nome == nome_aluno:
                    return f"Nome: {nome}\nSérie: {serie}\nEmail: {email}\nSenha: {senha}"
        return "Aluno não encontrado."
    except FileNotFoundError:
        return "Arquivo de alunos não encontrado."

def adicionar_aluno(nome, serie, email, senha):
    with open("alunos.txt", "a") as file:
        file.write(f"{nome},{serie},{email},{senha}\n")
    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")

def deletar_aluno(nome_aluno):
    try:
        with open("alunos.txt", "r") as file:
            linhas = file.readlines()
        with open("alunos.txt", "w") as file:
            for linha in linhas:
                aluno_nome, _, _, _ = linha.strip().split(',')
                if aluno_nome != nome_aluno:
                    file.write(linha)
        messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
    except FileNotFoundError:
        messagebox.showinfo("Erro", "Arquivo de alunos não encontrado.")
    except ValueError:
        messagebox.showinfo("Erro", "Erro ao processar o arquivo de alunos.")

# Funções da interface gráfica
def buscar_aluno():
    nome_pesquisado = entry_nome.get()
    resultado = buscar_informacoes_aluno(nome_pesquisado)
    messagebox.showinfo("Resultado da Pesquisa", resultado)

def adicionar_aluno_interface():
    nome = entry_nome.get()
    serie = entry_serie.get()
    email = entry_email.get()
    senha = entry_senha.get()
    
    if nome and serie and email and senha:
        adicionar_aluno(nome, serie, email, senha)
    else:
        messagebox.showinfo("Erro", "Preencha todos os campos.")

def deletar_aluno_interface():
    nome_pesquisado = entry_nome.get()
    deletar_aluno(nome_pesquisado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Alunos")

# Criar widgets
label_nome = tk.Label(janela, text="Nome do Aluno:")
entry_nome = tk.Entry(janela)

label_serie = tk.Label(janela, text="Série:")
entry_serie = tk.Entry(janela)

label_email = tk.Label(janela, text="Email:")
entry_email = tk.Entry(janela)

label_senha = tk.Label(janela, text="Senha:")
entry_senha = tk.Entry(janela, show="*")

botao_pesquisar = tk.Button(janela, text="Pesquisar", command=buscar_aluno)
botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_aluno_interface)
botao_deletar = tk.Button(janela, text="Deletar", command=deletar_aluno_interface)

# Posicionar widgets na janela
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_serie.grid(row=1, column=0, padx=10, pady=10)
entry_serie.grid(row=1, column=1, padx=10, pady=10)

label_email.grid(row=2, column=0, padx=10, pady=10)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_senha.grid(row=3, column=0, padx=10, pady=10)
entry_senha.grid(row=3, column=1, padx=10, pady=10)

botao_pesquisar.grid(row=4, column=0, pady=10)
botao_adicionar.grid(row=4, column=1, pady=10)
botao_deletar.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar a interface gráfica
janela.mainloop()
