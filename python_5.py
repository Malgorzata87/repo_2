#for i in range (0,10,1):
 #   print('Petla nr',i)
#for i in range (50, 20, -4):
 #   print('Petla nr',i)

sum = 0
for i in range (101):
    if i%2 == 0:
        sum += i
print(sum)

lista = [4, 34, 424, 354, 23, 232, 4, 426, 45]
for i in range (len(lista)):
    if lista[i] < 50:
        print(lista[i],'mniejsze od 50')
    else:
        print(lista[i], 'wieksze niz 50')