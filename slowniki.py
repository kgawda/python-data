slownik = {"Polska": "Warszawa", "Anglia": "Londyn"}
assert len(slownik) == 2
slownik["Indie"] = "Bombaj"
slownik["Indie"] = "Mumbaj"

assert slownik["Polska"] == "Warszawa"
# slownik["Francja"]  # KeyError: 'Francja'
assert slownik.get("Francja") == None
assert slownik.get("Francja", "nie wiadomo") == "nie wiadomo"
assert slownik.pop("Indie")  == 'Mumbaj' #  usuwa ze słownika, zwraca 'Mumbaj'

assert "Polska" in slownik  # czy klucz zawiera się w słowniku

for nazwa in slownik:  # tylko klucze
    print(nazwa)

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)

# poza .items() jest też: .keys() i .values()
