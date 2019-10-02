soma = 1

result = 0

for x in range(50):
	result = result+soma
	soma= soma+1

	print('{} + {}'.format(result, soma))

print('O resultado da soma é:', result)