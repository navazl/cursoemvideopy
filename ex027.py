nome = str(input("Digite seu nome completo: ")).strip().split() # strip tira os espaços, split corta a string e vira uma lista
print("Muito prazer em te conhecer! ")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[-1]}")