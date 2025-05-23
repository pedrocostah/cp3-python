def mostrar_duplas(nome, tupla_nomes):
    if nome in tupla_nomes:
        indice = tupla_nomes.index(nome)
        for i in range(indice + 1, len(tupla_nomes)):
            print(f"{nome} e {tupla_nomes[i]}")
nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

print("Duplas com a lista original:\n")
for nome in nomes:
    mostrar_duplas(nome, nomes)


print("\nAgora vamos adicionar um novo nome à lista.")
nome_novo = input("Digite um nome para adicionar: ")


nomes_atualizados = nomes + (nome_novo,)

print("\nDuplas com o nome adicionado:\n")
for nome in nomes_atualizados:
    mostrar_duplas(nome, nomes_atualizados)
