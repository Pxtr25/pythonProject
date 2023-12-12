while True:
    print("Wybierz działanie(+, -, *, /) lub napisz 0 aby zakończyć program")
    dzialanie = str(input())

    if(dzialanie=='+'):
        print("Podaj pierwszą liczbę: ")
        x = int(input())
        print("Podaj drugą liczbę: ")
        y = int(input())
        suma = x+y
        print("Wynik: ", suma)
    elif(dzialanie=='-'):
        print("Podaj pierwszą liczbę: ")
        x = int(input())
        print("Podaj drugą liczbę: ")
        y = int(input())
        różnica = x - y
        print("Wynik: ", różnica)
    elif (dzialanie == '*'):
        print("Podaj pierwszą liczbę: ")
        x = int(input())
        print("Podaj drugą liczbę: ")
        y = int(input())
        iloczyn = x * y
        print("Wynik: ", iloczyn)
    elif (dzialanie == '/'):
        print("Podaj pierwszą liczbę: ")
        x = int(input())
        print("Podaj drugą liczbę: ")
        y = int(input())
        if(y==0):
            print("Nie można dzielić przez zero")
        else:
            print("Podaj pierwszą liczbę: ")
            x = int(input())
            print("Podaj drugą liczbę: ")
            y = int(input())
            iloraz = x/y
            print("Wynik: ", iloraz)
    elif (dzialanie == '0'):
        break
    else:
        print("Wybierz poprawne działanie")