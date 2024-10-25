from math import sqrt

numero: int = int(input("Informe um numero inteiro: "))

if numero > 0:
    print(f'A raiz quadrada de {numero} eh {sqrt(numero)}')
else:
    print(f'O numero é invalido')