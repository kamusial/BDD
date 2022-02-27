import math

def add(x, y):
    return x + y


def no_of_letters(x):
    return len(x)


def fizzbuzz(number):
   if isinstance(number, int) and number > 0:
       if number%3 == 0 and number%5 == 0:
           return 'fizzbuzz'
       elif number%5 == 0:
           return 'buzz'
       elif number%3 == 0:
           return 'fizz'
       return str(number)
   return None


def playfizzbuzz(liczba):
   if isinstance(liczba, int) and x > 0:
       a = 0
       for i in range (1, liczba+1):
           print (f'{i} -> {fizzbuzz(i)}')
           a += i
       return i


def ileosob(liczba_osob, czy_sa_srodki):
   if isinstance(liczba_osob, int) and isinstance(czy_sa_srodki, bool) and liczba_osob > 0:
       if czy_sa_srodki:
           return math.floor(liczba_osob * 1.1)
       else:
           if liczba_osob == 1:
               return 1
           else:
               return math.floor(liczba_osob * 0.5)
   else:
       return None




