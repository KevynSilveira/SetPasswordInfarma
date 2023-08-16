
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from customtkinter import set_appearance_mode




frame = ctk.CTk()
frame.geometry("250x200")
frame.title("BoardPDF")
frame.resizable(False, False)
set_appearance_mode("Dark")

label_board_pdf = ctk.CTkLabel(master=frame, text="BoardPDF", width=150, height=30, text_color="white")
label_board_pdf.configure(font=("arial", 18))
label_board_pdf.place(x=50, y=5)

button_select = ctk.CTkButton(master=frame, text="Diretório origem", width=150, height=30, command=select, fg_color="dark grey", text_color="black", hover_color="gray")
button_select.configure(font=("arial", 14))
button_select.place(x=50, y=50)

entry_select = ctk.CTkEntry(master=frame, width=200, height=30)
entry_select.configure(font=("arial", 14))
entry_select.place(x=25, y=90)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30, command=execute, fg_color="dark grey", text_color="black", hover_color="gray")
button_execute.configure(font=("arial", 14))
button_execute.place(x=50, y=160)