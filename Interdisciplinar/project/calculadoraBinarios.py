#tkinter biblioteca para criar a interface grafica visivel ao usuário onde ele verá a calculadora sendo renderizada
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Importando canvas para image background
from PIL import ImageTk, Image


#Math serve para facilidade de chamadas das operações matemáticas
import math


################# cores ###############
co1 = "#feffff"  # white/branca
co3 = "#38576b"  # valor
fundo = "#e8e6e6" #branco cizentado
co10 ="#363434" #preto  claro


################# Config da janela #############

janela = Tk()
janela.title('Calculadora Cientifica')
janela.geometry('630x145')
janela.configure(bg=co1)


style = ttk.Style(janela)
style.theme_use("clam")


################ Imagem tiringa ###################

imagem = Image.open("./imagem/cearense.jpg")
imagem = imagem.resize((160, 140))  # Redimensiona a imagem para o tamanho da janela
imagem = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack()

label_imagem.place(x=240, y=0, relwidth=1, relheight=1)

################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_score = Frame(janela, width=478, height=56,bg=co3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=478, height=86,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)


################# Funções ####################

def entering_values(event):
	global all_values
	all_values = all_values + str(event)
	value_text.set(all_values)

def binary_calculator():
    global all_values

    binary1 = all_values.split()[0]  # Extrai o primeiro número binário
    binary2 = all_values.split()[2]  # Extrai o segundo número binário

    decimal1 = int(binary1, 2)  # Converte o primeiro número binário para decimal
    decimal2 = int(binary2, 2)  # Converte o segundo número binário para decimal

    # Realiza a operação matemática desejada nos números decimais
    if "+" in all_values:
        result_decimal = decimal1 + decimal2
    elif "-" in all_values:
        result_decimal = decimal1 - decimal2
    elif "*" in all_values:
        result_decimal = decimal1 * decimal2
    elif "/" in all_values:
        result_decimal = decimal1 // decimal2
    elif "%" in all_values:
        result_decimal = decimal1 % decimal2

    result_binary = bin(result_decimal)  # Converte o resultado decimal para binário
    value_text.set(result_binary)  # Exibe o resultado em binário na calculadora
    all_values = ""  # Limpa a variável all_values para a próxima operação
    
	

def scream_clear(): 
    global all_values
    all_values = "" 
    value_text.set("")

all_values = "" 
value_text = StringVar()

################# Label ####################

app_scream = Label(frame_score,width=33,height=2,textvariable = value_text , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Arial 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

################# Buttons ####################
b_1 = Button(frame_quadros, text="0", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('0'))
b_1.place(x=0, y=1)
b_2 = Button(frame_quadros, text="1", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('1'))
b_2.place(x=159, y=1)
b_3 = Button(frame_quadros, text="+", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('+'))
b_3.place(x=319, y=1)

b_4 = Button(frame_quadros, text="-", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('-'))
b_4.place(x=0, y=30)
b_5 = Button(frame_quadros, text="*", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('*'))
b_5.place(x=159, y=30)
b_6 = Button(frame_quadros, text="/", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('/'))
b_6.place(x=319, y=30)

b_7 = Button(frame_quadros, text="%", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('%'))
b_7.place(x=0, y=59)
b_8 = Button(frame_quadros, text="=", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = binary_calculator)
b_8.place(x=159, y=59)
b_9 = Button(frame_quadros, text="C", width=19, height=1, bg=co10, fg=fundo,font=('Arial 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: scream_clear())
b_9.place(x=319, y=59)

janela.mainloop()