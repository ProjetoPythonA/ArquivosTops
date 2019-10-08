mensagem = input('digite 0 para parar a lista, ENTER para seguir...')
n_pe = int(input('Qual a quantidade de pessoas ?'))
idade = int(input('digite a idade da pessoa :'))
i_menor = 0
i_maior = 0
while idade >= 1:
       idade = int(input('digite a idade da pessoa :'))
       if idade <= 17:
           i_menor += 1
       elif idade >18:
           i_maior += 1
total = i_menor + i_maior
porc_mai = (i_maior*100)/total
porc_men = (i_menor*100)/total
print('quantidades de pessoas cadastradas : {}'.format(n_pe))
print('porcentagem menor de 18, {:.2f}%'.format(porc_men))
print('porcentagem de maiores de 18, {:.2f}%'.format(porc_mai))