valorOne = float(input('Digite o primeiro valor: '))
valorTwo = float(input('Digite o segundo valor: '))
operacao = input("Digite a operação matematica, por exemplo: '\n'"
                     'SOMA = +,\n' 
                     'SUBTRAÇÃO = -, \n'
                      'MULTIPLICAÇÃO =  * \n'
                      'Divisão = / : ')

if operacao == 'SOMA' or operacao == 'soma' or operacao == '+':
    resultado = valorOne + valorTwo
    print('Sua soma da operação é: ', resultado)

elif operacao == 'SUBTRAÇÃO' or  operacao == 'subtracao' or operacao == 'SUBTRACAO' or operacao == '-':
    resultado = valorOne - valorTwo
    print('Sua subtração da operação é: ', resultado)

elif operacao == 'MULTIPLICAÇÃO' or operacao == 'multiplicação' or operacao == 'MULTIPLICACAO' or operacao == '*':
    resultado = valorOne * valorTwo
    print('Sua multiplicação da operação é: ', resultado)

elif operacao == 'DIVISÃO' or operacao == 'divisão' or operacao == 'divisao' or operacao == '/':
    resultado = valorOne // valorTwo
    print('Sua divisão da operação é: ', resultado)
else:
    print('Valores invalidos')
