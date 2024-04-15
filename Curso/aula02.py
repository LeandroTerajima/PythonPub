faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"Faturamento da empresa:{faturamento}, custo:{custo} , lucro:{lucro}")

email_cliente = "leandro.terajima@icloud.com"

# maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

#minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

#"@"
print("coluna do @", email_cliente.find("@"))

#tamanho do texto
print("tamanho do texto",len(email_cliente))

#pegaar o caracter
print(email_cliente[4])

print(email_cliente[-4])

#pegar pedaço do texto
print(email_cliente[:4])

#pegar parte do texte posição inicio / final
print(email_cliente[1:4])

#trocar um pedaço do texto
novo_email_cliente = email_cliente.replace("leandro.terajima", "terajima.leandro")
print(novo_email_cliente)

#trabalhar com nomes
nome = "leandro terajima"

print(nome.capitalize())
print(nome.title())

#pegar um servidor do e-mail
posicao_arroba = email_cliente.find("@") +1
servidor = email_cliente[posicao_arroba:]
print("Nomedo sservidor e-mail:",(servidor))


#pegar o 1o nome
posicao_espaco = nome.find(" ")
priomeiro_nome = nome[:posicao_espaco]

print("Primeiro nome do usuário:", (priomeiro_nome))


#pegaar o sobrenome
posicao_espaco = nome.find(" ") +1
sobrenome = nome[posicao_espaco:]

print("Sobrenome do usuário:",(sobrenome))


#casos especiais - nurmatações numericas em texto
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, custo: R${custo:.2f} , lucro: R${lucro:.2f}, Margem de lucro, {margem_lucro:.0%}")

