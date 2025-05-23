maior_valor = 0
maior_qtd = 0
produto_maior_qtd = ""
produto_maior_valor = ""

continuar = True

while continuar:
    produto = input("Produto (ENTER para sair):")
    if produto == "":
        continuar =  False
    else:
        quantidade = int(input("Quantidade: "))
        valor = float(input("Preço: "))

        if quantidade > maior_qtd:
            maior_qtd = quantidade
            produto_maior_qtd = produto
        if quantidade * valor > maior_valor:
            maior_valor = quantidade * valor
            produto_maior_valor = produto

print("Produto com maior quantidade: ", produto_maior_qtd)
print("Produto com maior valor em estoque: ", produto_maior_valor)