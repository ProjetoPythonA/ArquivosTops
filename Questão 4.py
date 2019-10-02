pessoas = 0
sexo = input('Digite o sexo. M para Masculino e F para feminino:')
masc = 0
femin = 0
while sexo == 'M' or sexo == 'F':
    if sexo == 'M':
        masc+= 1
    else:
        femin+= 1
    pessoas+= 1
    sexo = input('Digite o sexo. M para Masculino e F para feminino:')
print('Total de pessoas cadastradas:', pessoas)
print('Total de homens:', masc)
print('Total de mulheres:', femin)