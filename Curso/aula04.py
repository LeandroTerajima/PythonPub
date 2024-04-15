# condições
# condição se
# if condição/comparação: 
venda = 1500
meta = 1300

# operadores de comparação
# > maior que
# < menor que 
# >= maior ou igual 
# <= monor ou iguaal
# == igual
# != diferente

if venda > meta:
    print("vendedor fanha bônus")
    print("bateu a meta de vendas")
    bonus = 0.1 * venda
    print ("bbonus do vendedor: ", bonus)
else:
    print("vendedor não ganha bonus")
    print("não bateu a meta de vendas")

print("acabou o programa")

# segundo senário
vendas = 1500
vendas_empresa = 10000
meta_empresa = 20000
meta01 = 1300
meta02 = 2000

# Primeiro cenário de IF 

# if vendas >= 2000:
#     bonus = 0.13 * vendas 
# else:
#     if vendas >=1300:
#         bonus = 0.1 *vendas
#     else:
#         bonus = 0

# print("Bonus: ",bonus)

# segundo cenario usando elif 
if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas 
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
     bonus = 0.1 *vendas
else:
     bonus = 0

print("Bonus: ",bonus)

# condição usando uma lista

lista_produto = ["airpdo","ipad", "iphone", "macbbook"]
produto_procurado = input("Pesquise pelo produto: ")
produto_procurado = produto_procurado.lower

if produto_procurado in lista_produto:
    print("Produto em estoque")
else:
    print("não temos esse produto")
