# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# numero_Solicitado = int(input("Digite um número: "))

# divisao = numero_Solicitado/2

# check = str.find(str(divisao),".0")

# if check == 1:
#     print("Número é par")
# elif check == -1:
#     print("Número é impar")
# else:
#     print("Entrada invalida")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# idade = int(input("Por favor, insira sua idade: \n"))


# if idade >= 0 and idade <= 12:
#     print("Criança")
# elif idade >= 13 and idade <= 18:
#     print("Adolescente")
# elif idade > 18:
#     print("Adulto")    
# else:
#     print("Entrada Inválida")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# login = "abc"
# senha = "1234"

# i = 0
# while i == 0:
#     login_User = str(input("Insira seu login \n"))
#     senha_User = str(input("Insira sua Senha \n"))

#     if login == login_User and senha == senha_User:
#         print("Você está logado")
#         i += 1
#     else:
#         print("Usuário ou senha invalidos")
#         i == 0

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# i = 0
# while i == 0:

#     x = int(input("Digite as coordenadas de X: "))
#     y = int(input("Digite as coordenadas de y: "))

#     if x > 0 and y > 0:
#         print("Primeiro Quadrante")
#     elif x < 0 and y > 0:
#         print("Segundo Quadrante")
#     elif x < 0 and y < 0:
#         print("Terceiro Quadrante")
#     elif x > 0 and y < 0:
#         print("Quarto Quadrante")
#     else:
#         print("o ponto está localizado no eixo ou origem.")
#         i += 1
