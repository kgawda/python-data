lista = [1, 2, 3]

for liczba in lista:
    napis = "Liczba to " + str(liczba)
    print(napis)
# liczba i napis zachowują wartości z ostatniego przebiegu pętli

for znak in []:
    print(znak)
#print(znak)  # NameError: name 'znak' is not defined

for liczba in range(1, 4):  # 1 - chcę, 4 - nie chcę
    print(liczba)

dziwne_liczby = [1, 8, 3, 5, 7, 1, 10]
for indeks, liczba in enumerate(dziwne_liczby):
    # print("Indeks:", indeks, "Liczba:", liczba)
    if liczba == 5:
        print("Znalazłem piątkę! Jest pod indeksem", indeks)
        break

# tupla = 1, 2, 3  # zapakowanie
# a, b, c = tupla  # odpakowanie
# indeks, liczba = 0, 1  # takie odpakowanie jest robione przy enumerate

...