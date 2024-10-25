"""#Estruturas logicas: and, or, not, is

#Operadores unários:
    - not
Operadores binários:
    - and, or, id

AND - ambos valores devem ser True
OR - um ou outro valor devem ser True
NOT - valor do booleano é invertido. True > False, False > True
"""
ativo = True
logado = False

# Se não estiver ativo
if ativo is False:
    print('Você precisa ativar sua conta, necessário ativar conta')
else:
    print('Bem-vindo usuário')

#print(not False)