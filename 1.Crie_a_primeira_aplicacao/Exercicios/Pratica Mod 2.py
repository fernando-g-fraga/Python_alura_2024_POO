# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# numeros = [1,2,3,4,5,6,7,8,9,10]
# nomes = ["fernando", "douglas","jackeline"]
# ano = [1996,2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# for numero in numeros:
#     print(numero)

# # 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# soma = 0

# for numero in numeros:
#     if numero % 2 != 0:
#        soma = soma + numero
#        print(soma) 

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for numero in reversed(numeros):
#     print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# user_input = int(input("Digite um numero para ser calculado"))

# for i in range(1,11):
#     print(user_input * i) 

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# numeros = [1, 2,3,4,5,6,7,8,"abc",10]
# soma = 0
# try: 
#     for i in numeros:
#         soma = soma + i
#         print(soma)
# except:
#     print('Entrada inválida')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1, 2,3,4,5,6,7,8,0,10]
media = 0

try:
    for i in numeros:
        media = media + i
    
    media = media/len(numeros)
    print (media)

except:
    print("divisão por zero")