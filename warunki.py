liczba = 5
napis = "Ala ma kota"
znaki = ""
lista = [1, 2, 3]
tupla = (1, 2, 3)

if liczba == 1:
    print("Gratuluję, liczba jest 1.")
elif 6 < len(napis) < 100:
    print("Długi napis (ale nie przesadnie długi)")
elif znaki:
    print("Mamy jakieś znaki")
else:
    print("Inny przypadek")

assert 1 in lista
assert 5 not in lista
assert 1 in tupla
assert 5 not in tupla
assert "Ala" in napis  # uwaga! działa inaczej niż dla list/tupple, czy dany kawałek pojawia się w tekście
