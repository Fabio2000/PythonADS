#Biblioteca de renderização da tela
from tkinter import *
from tkinter import ttk

#Configuraçãoes da tela tenderizada pelo tkinter
janela = Tk()
janela.title("Conversor")
janela.geometry("500x218")

#Função de converção decimal para binário
def conversao_binario():
    decimal = int(entry_valor.get())
    if decimal == 0:
        label_resultado.config(text='0')
        return
    binario = bin(decimal)[2:] # chamada da função bin() e convertendo para 0 e 1
    label_resultado.config(text=binario)
pass

# Função para conversão decimal para octal
def conversao_octal():
    decimal = int(entry_valor.get())
    if decimal == 0:
        label_resultado.config(text='0')
        return
    octal = oct(decimal)[2:] # chamada da função oct() e remoção dos dois primeiros caracteres ('0o')
    label_resultado.config(text=octal)
pass

# Função para conversão decimal para hexadecimal
def conversao_hexa():
    decimal = int(entry_valor.get())
    if decimal == 0:
        label_resultado.config(text='0')
        return
    hexa = hex(decimal)[2:] # chamada da função hex() e e remoção dos dois primeiros caracteres ('0x')
    label_resultado.config(text=hexa)
pass

#Função para limpar os campos de entrada e resultado
def limpar():
    entry_valor.delete(0, END)
    label_resultado.config(text='')
pass

# config dos widgets
Label_valor = Label(
    janela, text='Digite um numero: ', font=('Arial 15 bold'))
Label_valor.place(x=40, y=10)

# input valor
entry_valor = Entry(janela, borderwidth=1, relief="solid",
                    fg="black", bg='#D3D3D3', font=('Arial 15 bold'))
entry_valor.place(x=225, y=12, width=230)

# Botão de conversão decimal para binário
button_binario = Button(janela, text='Binário',
                        font=('Arial 15 bold'), bg='#90EE90', command=conversao_binario)
button_binario.place(x=5, y=65, width=155)

# Botão de conversão decimal para Octal
button_octal = Button(janela, text='Octal', font=(
    'Arial 15 bold'), bg='#90EE90', command=conversao_octal)
button_octal.place(x=170, y=65, width=155)

# Botão de conversão decima para Hexadecimal
button_hexa = Button(janela, text='Hexadecial',
                     font=('Arial 15 bold'), bg='#90EE90', command=conversao_hexa)
button_hexa.place(x=340, y=65, width=155)

# Botão de resultado
label_resultado_texto = Label(
    janela, text='Resultado operação:', font=('Arial 14 bold'))
label_resultado_texto.place(x=40, y=125)
label_resultado = Label(janela, text='', font=('Arial 15 bold'), width=38,
                        height=1, borderwidth=1, relief="solid", fg="black", bg='#D3D3D3')
label_resultado.pack(padx=10, pady=10)
label_resultado.place(x=245, y=125, width=210)

#Botão para limpar os valores digitados no input
button_limpar = Button(janela, text='Limpar', bg='#FFB6C1', font=('Arial 12 bold'), command=limpar)
button_limpar.pack(padx=10, pady=10)
button_limpar.place(x=40, y=170, width=415)


janela.mainloop()