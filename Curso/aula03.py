#imput
email=input("escreva seu e-mail: ")
nome= input("seu primeirto nome: ")
print(nome)
print(email)

print(f"{nome}, verifique seu e-mail: {email} que enviamos um link de")

# faturamento = float(input("Informe o faturamento: "))
# imposto = faturamento * 0.1
# print(imposto)

#listas

vendas =[ 100 , 50 , 14 , 20 , 700]

# soma dos elementos
total_vendas = sum(vendas)
print (total_vendas)
# verificar tamanho da lista
quantidade_vendas = len(vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar posição na lista
print(vendas[0])
print(vendas[-1])

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]
produto_procurado =input("Pesuise pelo nome do produto: ")
produto_procurado = produto_procurado.lower
print("apple watch" in lista_produtos)


# adicionar item na lista
lista_produtos.append("apple watch")
print(lista_produtos)
# remover um item na lista
lista_produtos.remove("apple watch")
print(lista_produtos)
# remover posição da lista
lista_produtos.pop(0)
print(lista_produtos)
# editar um item na lista
precos = [1000, 1500, 3500]
# editar valor direto
# precos[0] = 6000
# editar valor calculando
precos[0] =precos[0] * 1.5
print(precos)

# contar quantaas vezes um item aparece na lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "macbook", "macbook", "iphone"]
print(lista_produtos.count("iphone"))

# ordenar uma lista
# ordenar de foma decrescente passar o paremetro reverse=true
# lista_produtos.sort(reverse=True)
lista_produtos.sort()
print(lista_produtos)
