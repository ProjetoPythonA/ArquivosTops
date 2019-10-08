par = 0
impar = 0
x = 0
n = int(input('digite um número: '))
while n != 0:
   n = int(input("Digite um número: "))
   if n % 2 == 0:
       par += 1
   else:
       impar += 1
   x += 1
print(f'Você digitou{par}números pares.')
print(f'Você digitou {impar}número ímpares.')