sexo = str(input('Digite o seu sexo M/F: ')).strip().upper()
while sexo not in 'MF':
	sexo = str(input('Dados invalidos digite novamente M/F: ')).strip().upper()
print(f'Sexo {sexo} registrado!')