
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import set_appearance_mode




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
entry_code.configure(font=("arial", 10))
entry_code.place(x=25, y=90)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30, fg_color="dark grey", text_color="black", hover_color="gray")
button_execute.configure(font=("arial", 14))
button_execute.place(x=50, y=160)


frame.mainloop()