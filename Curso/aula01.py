faturamento = 1200
custo = 750.0
novas_vendas = 100
imposto = faturamento * 0.1
faturamento = faturamento + novas_vendas


lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("Faturamento foi de:", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de:", lucro)
print("A margemde  lucro foi de:", round (margem_lucro,2))

print (10 % 3)