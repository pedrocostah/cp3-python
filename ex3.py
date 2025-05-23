nomes = ("Pedro", "Julia", "Matheus", "Caio", "Thais")

soma = 0

for nome in nomes:
    soma += 1

i = 0
while i < soma:
    j = i + 1
    while j < soma:
        print(nomes[i], "e", nomes[j])
        j += 1
    i += 1