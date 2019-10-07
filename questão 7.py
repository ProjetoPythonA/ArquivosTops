numMaior = 0
num = int(input('Digite um numero inteiro:'))
while num > 0:
    if num > numMaior:
        numMaior = num
        num = int(input('valor:'))
print("O Maior Número é {}" .format(numMaior))