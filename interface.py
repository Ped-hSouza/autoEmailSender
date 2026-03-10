import os
from dotenv import load_dotenv

import tkinter as tk
from tkinter import ttk, messagebox

from Agendamento import Agendamento
from enviar_email import enviar_email

#carrega as variáveis de ambiente
load_dotenv()


#Função disparar_agendamento -> Instancia a classe agendamentoe passa a instância para a função enviar_email junto com as informações de login.
def disparar_agendamento():

    try:
        email = entry_email.get()
        nome = entry_nome.get()
        neuropediatra = opcoes_neuropediatras.get()
        data = entry_data.get()
        hora = entry_hora.get()

        agendamento = Agendamento(email, nome, neuropediatra, data, hora)

        #pega as variávis de ambiente
        email_password = os.getenv("EMAIL_PASS")
        email_adress = os.getenv("EMAIL_USER")

        enviar_email(agendamento, email_adress, email_password)

        messagebox.showinfo("Sucesso!", "O e-mail foi enviado com sucesso!")

    except Exception as erro:

        messagebox.showerror("Erro ao enviar", f"Houve um problema: {erro}")

# Opções de neuropediatra
neuropediatras = ['Caroline', 'Jório', 'Pedro']

#config da interface
root = tk.Tk()
root.title("Automação de E-mails")
root.geometry("600x700")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#frame do formulário
frame_central = tk.Frame(root)
frame_central.grid(row=0, column=0)

# CAMPO DO E-MAIL
tk.Label(frame_central, text="E-mail do Destinatário:", font=("Arial", 10, "bold")).grid(column=0, row=0, pady=5, padx=5, sticky="e")
entry_email = tk.Entry(frame_central, width=40)
entry_email.grid(column=1, row=0)

#CAMPO DO NOME
tk.Label(frame_central, text="Nome do paciente:", font=("Arial", 10, "bold")).grid(column=0, row=1, pady=5, padx=5, sticky="e")
entry_nome = tk.Entry(frame_central, width=40)
entry_nome.grid(column=1, row=1)

#CAMPO DO NEUROPEDIATRA
tk.Label(frame_central, text="Neuropediatra:", font=("Arial", 10, "bold")).grid(column=0, row=2, pady=5, padx=5, sticky="e")
opcoes_neuropediatras = ttk.Combobox(frame_central, values=neuropediatras, width=37)
opcoes_neuropediatras.grid(column=1, row=2)
opcoes_neuropediatras.set('Escolha o neuropediatra')

#CAMPO DE DATA
tk.Label(frame_central, text="Data:", font=("Arial", 10, "bold")).grid(column=0, row=3, pady=5, padx=5, sticky="e")
entry_data = tk.Entry(frame_central, width=40)
entry_data.grid(column=1, row=3)
entry_data.insert(0, "DD/MM/AAAA")

#CAMPO DE HORÁRIO
tk.Label(frame_central, text="Horário:", font=("Arial", 10, "bold")).grid(column=0, row=4, pady=5, padx=5, sticky="e")
entry_hora = tk.Entry(frame_central, width=40)
entry_hora.grid(column=1, row=4)
entry_hora.insert(0, "00:00")

#BOTÃO DE ENVIAR

botao_enviar = tk.Button(frame_central, text="Enviar e-mail", command=disparar_agendamento)
botao_enviar.grid(columnspan=2, column=0, row=5, pady=30)



root.mainloop()