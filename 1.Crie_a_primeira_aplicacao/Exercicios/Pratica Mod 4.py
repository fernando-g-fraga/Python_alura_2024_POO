# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = {"nome":"Fernando","idade":"27","cidade":"são paulo"}
# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoas.update({"idade":"18"})
print(pessoas)
# Adicione um campo de profissão para essa pessoa;
pessoas["profissao"] = "mecanico" 
print(pessoas)
# Remova um item do dicionário.
pessoas.pop("idade")
print(pessoas)
# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
quadrados = {x: x**2 for x in range(1,6)}
print(quadrados)
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dic = {"chave 1":"teste","chave2":"teste 2"}
if "chave 1" in dic:
    print("a chave foi encontrada")
else:
    print("a chave não foi encontrada")
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.    
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

numero_palavras = {}
palavras = frase.split()

for palavra in palavras:
    numero_palavras[palavra] = numero_palavras.get(palavra,0)+1

print (numero_palavras)
