#Biblioteca para renderização da tela em executavel(.exe)
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo

# #Importando canvas para image background
#from PIL import ImageTk, Image

# Função para converter um número binário para decimal
def binario_para_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        digito = int(binario[len(binario) - 1 - i])
        decimal += digito * (2 ** i)
    return decimal

# Função para converter um número decimal para binário
def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario

# Função para realizar a soma de dois números binários
def soma_binaria():
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    resultado = binario_para_decimal(binario1) + binario_para_decimal(binario2)
    resultado_binario = decimal_para_binario(resultado)
    label_resultado.config(text=resultado_binario)

# Função para realizar a subtração de dois números binários
def subtracao_binaria():
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    resultado = binario_para_decimal(binario1) - binario_para_decimal(binario2)
    resultado_binario = decimal_para_binario(resultado)
    label_resultado.config(text=resultado_binario)

# Função para realizar a multiplicação de dois números binários
def multiplicacao_binaria():
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    resultado = binario_para_decimal(binario1) * binario_para_decimal(binario2)
    resultado_binario = decimal_para_binario(resultado)
    label_resultado.config(text=resultado_binario)

# Função para realizar a divisão de dois números binários
def divisao_binaria():
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    if binario_para_decimal(binario2) == 0:
        mostrar_erro_divisao_por_zero()
        return
    resultado = binario_para_decimal(binario1) // binario_para_decimal(binario2)
    resultado_binario = decimal_para_binario(resultado)
    label_resultado.config(text=resultado_binario)

# Função para mostrar uma mensagem de erro em caso de divisão por zero
def mostrar_erro_divisao_por_zero():
    showinfo('Erro', 'Divisão por zero não é suportada.')

# Configurações da janela
app = Tk()
app.title('Calculadora Binária')
app.geometry('800x300')

################ Imagem tiringa ###################
# imagem = Image.open("./imagem/cearense.jpg")
# imagem = imagem.resize((160, 160))  # Redimensiona a imagem para o tamanho da janela
# imagem = ImageTk.PhotoImage(imagem)

# label_imagem = tk.Label(app, image=imagem)
# label_imagem.pack()

# label_imagem.place(x=250, y=-90, relwidth=1, relheight=1)

# Configurações dos widgets
#Label Texto Valor 1
label_binario1 = Label(app, text='Digite o primeiro número binário:', font=('Arial 15 bold'))
label_binario1.pack()
label_binario1.place(x=0, y=5)

#INPUT VALOR 1
entry_binario1 = Entry(app, borderwidth=1, relief="solid", fg="black", bg='#D3D3D3', font=('Arial 15'))
entry_binario1.pack()
entry_binario1.place(x=320, y=8, width=200)


#Label Texto Valor 2
label_binario2 = Label(app, text='Digite o segundo número binário:', font=('Arial 15 bold'))
label_binario2.pack()
label_binario2.place(x=0, y=48)

#INPUT VALOR 2
entry_binario2 = Entry(app, borderwidth=1, relief="solid", fg="black", bg='#D3D3D3', font=('Arial 15'))
entry_binario2.pack()
entry_binario2.place(x=320, y=50, width=200)

#Botão de soma
button_soma = Button(app, text='Soma', font=('Arial 15 bold'), bg='#90EE90', command=soma_binaria)
button_soma.pack()
button_soma.place(x=15, y=135, width=170)

#Botão de subtração
button_subtracao = Button(app, text='Subtrair', font=('Arial 15 bold'), bg='#90EE90', command=subtracao_binaria)
button_subtracao.pack()
button_subtracao.place(x=210, y=135, width=170)

#Botão de multiplicação
button_multiplicacao = Button(app, text='Multiplicar', bg='#90EE90', font=('Arial 15 bold'), command=multiplicacao_binaria)
button_multiplicacao.pack()
button_multiplicacao.place(x=410, y=135, width=170)

#Botão de divisão
button_divisao = Button(app, text='Dividir', font=('Arial 15 bold'), bg='#90EE90', command=divisao_binaria)
button_divisao.pack()
button_divisao.place(x=610, y=135, width=170)

#Botão de resultado
label_resultado_texto = Label(app, text='Resultado das operações:', font=('Arial 15 bold'))
label_resultado_texto.place(x=80, y=200)
label_resultado = Label(app, text='', font=('Arial 15 bold'), width=38, height=1, borderwidth=1, relief="solid", fg="black", bg='#D3D3D3')
label_resultado.pack(padx=10, pady=10)
label_resultado.place(x=335, y=200, width=400)

#Função para limpar os campos de entrada e resultado
def limpar():
    entry_binario1.delete(0, END)
    entry_binario2.delete(0, END)
    label_resultado.config(text='')
pass

#Botão para limpar os valores digitados no input
button_limpar = Button(app, text='Limpar', bg='#FFB6C1', font=('Arial 12 bold'), command=limpar)
button_limpar.pack(padx=10, pady=10)
button_limpar.place(x=265, y=250, width=300)

app.mainloop()