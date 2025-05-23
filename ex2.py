texto = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
soma = 0

for letra in texto:
    if letra in vogais:
        soma += 1

print("Quantidade de vogais:", soma)