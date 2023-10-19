print("Calculadora de IMC")
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / altura**2
print('Seu IMC é: %.3f' %imc)
if imc < 16:
    print("Magreza grave\n")
elif imc < 17:
    print('Magreza moderada\n')
elif imc < 18.5:
    print('Magreza leve\n')
elif imc < 25:
    print('Saudável\n')
elif imc < 30:
    print('Sobrepeso\n')
elif imc < 35:
    print('Obesidade Grau I\n')
elif imc < 40:
    print('Obesidade Grau II (Severa)\n')
else:
    print('Obesidade Grau III (Morbidade)\n')
