pequena = 0

normal = 0

alta = 0

quant = 1


altur = float(input('Digite a altura da pessoa:'))

while altur > 0 and altur < 3.00:
    
	if altur < 1.59:
        
		pequena+= 1
    
	elif altur > 1.60 and altur < 1.79:
        
		normal+= 1
    
	else:
        
		alta+= 1
    
	quant+= 1
    
	altur = float(input('Digite a altura da pessoa {}:' .format(quant)))
    

print('Você digitou um número incorreto ou maior que 3 metros!')

print('Pessoas menores que 1.60:', pequena)

print('Pessoas com altura entre 1.60 e 1.79:', normal)

print('Pessoas com altura maior ou igual a 1.80:', alta)