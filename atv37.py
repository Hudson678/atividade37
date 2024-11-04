#Ler um vetor com 20 idades e exibir a maior e menor.

idade = []

for idd in range(20):
    idades = int(input(f"digite a idade {idd + 1}: "))
    idade.append(idades)

maior = max(idade)
menor = min(idade)
print (f"o maior numero é {maior}")
print (f"o maior numero é {menor}")
