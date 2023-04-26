#Import da biblioteca que renderiza o executavel
from tkinter import *
from tkinter import ttk

#Configaraçãos dimensções da tela, e titulo
janela = Tk()
janela.title("Exercicio um python faculade")
janela.geometry("610x280")

#Funções para cacular os valores

def calcular():

    branco = int(entry_brancos.get())
    vermelho = int(entry_vermelhos.get())
    codorna = int(entry_codorna.get())

    resultadoB = branco*0.95
    resultadoV = vermelho*1.05
    resultadoC = codorna*5.75
    total = resultadoB+resultadoC+resultadoV

    label_resultado.config(text='Lucros ovos brancos: R$' + str(resultadoB) + '\n' 
                           + 'Lucros ovos vermelhos: R$' + str(resultadoV) + '\n' 
                           + 'Lucros duzia codorna: R$' + str(resultadoC) + '\n' 
                           + 'Total arrecadado: R$' + str(total))




#Titulo
label_resultado = Label(janela, text='GRANJA LITTLE', font=('Arial 22 bold'))
label_resultado.place(x=230, y=5)


#Configuração label ovos brancos
Label_brancos = Label(janela, text='R$0,95 ovo branco: ', font=('Arial 15 bold'))
Label_brancos.place(x=5, y=60)
#Configuração input ovos brancos
entry_brancos = Entry(janela, borderwidth=1, width=6, relief="solid",
                    fg="black", bg='#D3D3D3', font=('Arial 15 bold'))
entry_brancos.place(x=208, y=63)



#Configuração label ovos codorna
Label_codorna = Label(janela, text='R$5,75 Duzia codorna: ', font=('Arial 13 bold'))
Label_codorna.place(x=5, y=103)
#Configuração input ovos codorna
entry_codorna = Entry(janela, borderwidth=1, width=6, relief="solid",
                    fg="black", bg='#D3D3D3', font=('Arial 15 bold'))
entry_codorna.place(x=208, y=103)



#Configuração label ovos vermelho
label_vermelhos = Label(janela, text='R$1,05 ovos vermelhos: ', font=('Arial 13 bold'))
label_vermelhos.place(x=5, y=140)
#Configuração input ovos vermelho
entry_vermelhos = Entry(janela, borderwidth=1, width=6, relief="solid",
                    fg="black", bg='#D3D3D3', font=('Arial 15 bold'))
entry_vermelhos.place(x=208, y=143)

#Configuração label de resultado
label_resultado = Label(janela, text='', font=('Arial 12 bold'), width=38,
                        height=1, borderwidth=1, relief="solid", fg="black", bg='#D3D3D3', justify='right')
label_resultado.pack(padx=10, pady=10)
label_resultado.place(x=300, y=63, width=290, height=109)


#Configuração botão calcular 
button_calcular = Button(janela, text='Calcular', bg='#19e67f', font=('Arial 12 bold'), command=calcular)
button_calcular.place(x=300, y=178, width=287)




janela.mainloop()