napis = "Ala ma kota"
assert napis.upper() == "ALA MA KOTA"
assert napis.lower() == "ala ma kota"
assert napis[0] == "A"

imie = "Ala"
koty = 2
napis_zrobion_przez_fstring = f"{imie} ma {koty} koty. To razem {2 + 4 * koty} nóg."
print(napis_zrobion_przez_fstring)

assert "Ala" in napis
assert "ala" not in napis
assert "ala" != "Ala"

tresc1 = "Pan Tadeusz\nLitwo! ..."
tresc2 = """Pan Tadeusz
Litwo! ..."""
if True:
    tresc3 = """Pan Tadeusz
Litwo! ..."""  # Uwaga! Jeśli damy tu spacje na początku, to będą one częścią napisu

assert tresc1 == tresc2 == tresc3
