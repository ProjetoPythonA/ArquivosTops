soma = 0.0

prod = 1

for x in range(10):
    
	numero = float(input('Digite o preço do produto {} :'.format(prod)))

	soma+=numero

	prod = prod+1

 
print('A soma de todos os produtos é de: R${}'.format(soma))