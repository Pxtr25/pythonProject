# porównywanie liczb
# print("Podaj pierwszą liczbe")
# x = input()
# print("Podaj drugą liczbe")
# y = input()
# if x > y:
#     print(x, "jest większe od", y)
# else:
#     print(y, "jest większe od", x)


#najwieksze i najmniejsze liczby z tablicy
# liczby = [4, 5, 1, 19, -3, -5]
#
# min = None
# max = None
#
# for x in liczby:
#     if min == None or min > x:
#         min = x
#     if max == None or max < x:
#         max = x
#
# print("Najmniejsza liczba z tablicy to: ", min, "a największa to: ", max)

# zgadywanie liczby
#
# import random
#
# x = (random.randint(0,100))
# i = 0
# print("Podaj liczbe od 0 do 100")
# while i < 10:
#     y = int(input())
#     if y > 100 or y < 0:
#         print("podaj poprawną liczbę!!!")
#     else:
#         if x > y:
#             print("liczba jest większa")
#             i+=1
#
#         elif y > x:
#             print("Liczba jest mniejsza")
#             i += 1
#
#         elif y == x:
#             print("Wygrałeś gratulacje!!!")
#             i += 1
#             break
#
# if i == 10:
#     print(" ")
#     print("Przegrałeś!!!")
#

# podajemy wiek
#
# from datetime import datetime
#
# data = datetime.now()
#
# rok = data.year
#
# print("Podaj imie: ")
# imie = input()
# print("Podaj nazwisko: ")
# nazwisko = input()
# print("Podaj rok ur: ")
# ur = int(input())
# while ur > rok:
#     print("Podaj poprawny rok!!!")
#     ur = int(input())
#
# wiek = rok - ur
# print(imie, " twój wiek to: ", wiek)

# proste dzialania

# import math
#
# print("Podaj pierwszą liczbę: ")
# x = int(input())
# print("Podaj drugą liczbe: ")
# y = int(input())
#
# print("Suma: ", x+y)
# print("Różnica: ", x-y)
# print("Iloczyn: ", x*y)
# print("Iloraz: ", x/y)
# print("Pierwiastek z sumy: ", math.sqrt(x+y))
# print("x do potegi y: ", x**y)
# print("y do potegi x: ", y**x)

# pole i obwod kola
# import math
# pi = math.pi
#
# print("Podaj promień okręgu: ")
# r = int(input())
#
# while r < 0:
#     print("Podano złą wartość")
#     r = int(input())
# pole = (pi)*(r**2)
# obwod = 2*pi*r
#
# print("Pole tego koła to: ", round(pole, 2), " a obwód to: ", round(obwod, 2))


#prosty kalkulator

import math

print("Podaj pierwszą liczbę: ")
x = int(input())
print("Podaj drugą liczbe: ")
y = int(input())
print("Podaj dzialanie: ")
dzialanie = str(input())

# if dzialanie == '+':
#     print("Wynik dodawania: ", x+y)
# elif dzialanie == '-':
#     print("Wynik odejmowania: ", x-y)
# elif dzialanie == '*':
#     print("Wynik mnożenia: ", x*y)
# elif dzialanie == '/':
#     if y == 0:
#         print("Nie wolno dzielić przez zero!!!")
#     else:
#         print("Wynik dzielenia: ", x/y)
# else:
#     print("Podaj dobre działanie!!!")

match dzialanie:
    case '+':
        print("Wybrano dzialanie: ", x+y)
    case '-':
        print("Wybrano odejmowanie: ", x-y)
    case '*':
        print("Wybrano mnożenie: ", x*y)
    case '/':
        if y == 0:
            print("Nie wolno dzielić przez zero!!!")
        else:
            print("Wybrano dzielenie", x/y)
    case _:
        print("Podano złe działanie")


# przeliczanie temperatury
#
# print("Podaj temperature w kelvinach: ")
# kel = int(input())
#
# cel = kel - 273.15
# print("Podana temperatura w Celsjuszach wynosi: ", cel)


