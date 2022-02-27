from functions import *

x = int(input('Podaj liczbe '))
y = int(input('O ile zwiekszamy '))
print('Liczba ', x, ' zwiekszona o ', y, ' wynosi ', add(x, y))

x = input('Podaj slowo ')
print('Ilosc znakow w slowie wynosi ', no_of_letters(x))

x = int(input('Do ilu gramy w FizzBuzz?  '))
for i in range(1, x + 1):
    print(i, ' -> ', fizzbuzz(i))
