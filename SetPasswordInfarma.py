import customtkinter as ctk
import pyodbc
from tkinter import messagebox
from customtkinter import set_appearance_mode

def access_db(): # Acessa o banco de dados
    global conn, cursor  # Utiliza as variáveis globais

    try:
        # Credenciais do banco de dados
        server = ""
        database = ""
        username = ""
        password = ""

        # Monta os dados para enviar para o banco de dados (credenciais)
        conn_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
    except:
        messagebox.showerror("ATENÇÃO", "Erro ao conectar no banco")
    return conn, cursor

def close_db(): # Fecha a conexão com o banco de dados.
    global conn, cursor  # Utiliza as variáveis globais
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()

def update_db(IdLogin): # Faz o update
    global cursor # Pega o cursor global

    try:
        query_update =f"update usuar set Senha_Hash = '251774b06c4954385a8ca96bb7eb644d' where Isn = {IdLogin}"

        cursor.execute(query_update) # Executa a query
        conn.commit() # Confirma o update

        rows_affected = cursor.rowcount # Verifica quantas linhas foram afetadas
        messagebox.showinfo("ATENÇÃO", f"Foram afetadas {rows_affected} linhas!")
        print(f"Foram afetadas {rows_affected} linhas!")
        return rows_affected # Retorna o valor da linha para armazenar em uma variavel

    except pyodbc.Error as e:
        messagebox.showerror("ATENÇÃO", f"Erro ao executar a consulta no banco de dados: {e}")

def execute():
    try:
        code = entry_code.get()
        if code:
            print(code)
            access_db()
            rows_affected = update_db(code)
            if rows_affected == 0:
                messagebox.showerror("ATENÇÃO", "Digite um id válido.")
            close_db()
        else:
            messagebox.showerror("ATENÇÃO", "Preencha todos os campos!")
    except Exception as e:
        error_message = f"Ocorreu um erro: {str(e)}"
        messagebox.showerror("ERRO", error_message)


frame = ctk.CTk()
frame.geometry("250x200")
frame.title("BoardPDF")
frame.resizable(False, False)
set_appearance_mode("Dark")

label_set_password = ctk.CTkLabel(master=frame, text="SetPassword", width=150, height=30, text_color="white")
label_set_password.configure(font=("arial", 18))
label_set_password.place(x=50, y=5)

label_set_password = ctk.CTkLabel(master=frame, text="Insira o código de login:", width=150, height=30, text_color="white")
label_set_password.configure(font=("arial", 14))
label_set_password.place(x=50, y=65)

entry_code = ctk.CTkEntry(master=frame, width=200, height=30)
entry_code.configure(font=("arial", 12), justify="center")
entry_code.place(x=25, y=90)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30, fg_color="dark grey", text_color="black", hover_color="gray", command=execute)
button_execute.configure(font=("arial", 14))
button_execute.place(x=50, y=160)

frame.mainloop()