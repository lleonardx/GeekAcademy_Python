numero1 : int = int(input("Informe primeiro numero: "))
numero2 : int = int(input("Informe primeiro numero: "))

if numero1 > numero2:
    print(f'O numero {numero1} eh maior que o {numero2}')
elif numero1 == numero2:
    print(f'Os numeros {numero1} e {numero2} são iguais')
else:
    print(f'O numero {numero2} eh maior que o numero {numero1}')
