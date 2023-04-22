idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Você não está apto para o direito de voto, sua idade é: ', idade)

elif idade >= 18 & idade <= 65:
    print('Seu voto é obrigátorio, pois sua idade é: ', idade)

elif idade >= 16 or idade >= 18 and idade <= 65:
    print('Você é um eleitor facultativo: ', idade)
pass