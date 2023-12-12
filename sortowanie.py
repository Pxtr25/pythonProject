import random
tablica = random.sample(range(1, 100), 5)
# wylosuj 5 liczb i wprowadź je do tablicy
print("Tablica nieposortowanych liczb: ", tablica)
tablica.sort()
print("Tablica posortowanych liczb: ", tablica)
