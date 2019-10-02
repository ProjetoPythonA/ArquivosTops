idade = 0
media = 0
soma = 0
for idade in range(10):
    idade = int(input('Digite a idade:'))
    soma += idade

media = soma / 10
print('a média eh', media)
