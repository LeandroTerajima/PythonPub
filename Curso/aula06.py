# dicionário do python
# lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
# precos_produtos = [2000, 9000, 6000, 11000]
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# pegar um elemento, se utiliza a chave
print(dic_produtos["iphone"])

# editar elemento
dic_produtos["iphone"] = dic_produtos["iphone"] *1.3
print(dic_produtos)

# quantidade dos itens
print(len(dic_produtos))

# reirar um item do dicionário
dic_produtos.pop("airpod")
print(dic_produtos)

# adicionar um item no dicionário
dic_produtos["apple watch"] = 25000
print(dic_produtos)

# verificar se um item existe no dicionário
# pesquisa pela chave
if "iphone" in dic_produtos:
    print("Existe o produto")
else:
    print("Não existe")

# verificar se uma chave existe no discionário


# verificar se um valor existe nos valores do discionário
if 9000 in dic_produtos.values():
    print("Existe")
else:
    print("Não existe")

nome_produto = input("Nome do produto: ")
preco_produto =input("Preço do produto")

# cadastrar o novo produto (se o produto não existir)
# caso o produto exista, editar o produto
nome_produto = nome_produto.lower()
preco_produto =  float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

# além disso: o prgrama tem que no final atualizar o preço de todos os produtos para
# os novos valores que são 10% a mais que os preços originais

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)

