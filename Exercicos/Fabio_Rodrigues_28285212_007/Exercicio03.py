produto = str(input('Digite o nome do produto: '))

valor = float(input('Digite o valor do produto: '))

if valor < 10:
    valorDois = valor * 70 // 100
    resultado = valor + valorDois
    print('Seu produto:', produto, '\n' 
          'Tem o valor de compra de:', valor, '\n' 
          'Tera o lucro de:', valorDois, '\n' 
          'Tera o valor total de:', resultado)
    
elif valor <= 10 or valor < 30:
    valorDois = valor * 50 // 100
    resultado = valor + valorDois
    print('Seu produto:', produto, '\n' 
          'Tem o valor de compra de:', valor, '\n' 
          'Tera o lucro de:', valorDois, '\n' 
          'Tera o valor total de:', resultado)
    
elif valor <= 30 or valor < 50:
    valorDois = valor * 40 // 100
    resultado = valor + valorDois
    print('Seu produto:', produto, '\n' 
          'Tem o valor de compra de:', valor, '\n' 
          'Tera o lucro de:', valorDois, '\n' 
          'Tera o valor total de:', resultado)
    
elif valor >= 50:
    valorDois = valor * 30 // 100
    resultado = valor + valorDois
    print('Seu produto:', produto, '\n' 
          'Tem o valor de compra de:', valor, '\n' 
          'Tera o lucro de:', valorDois, '\n' 
          'Tera o valor total de:', resultado)
pass