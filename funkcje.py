def powitaj_swiat():
    print("Hello world!")
    # Trzy równoznaczne rzecz y:
    #   # brak return (jeśli jesteśmy na końcu funkcji)
    #   return
    #   return None

def powitaj(imie):
    print(f"Witaj {imie}!")

def pole_kwadratu(bok):
    print("Rozpoczynam funkcję")
    wynik = bok ** 2
    return wynik

def pole_prostokata(a, b):
    return a * b

def pole_wielu_kwadratow(bok, liczba):
    return liczba * pole_kwadratu(bok)


powitaj_swiat()
powitaj("Konrad")
powitaj("nieznajomy")

pole = pole_kwadratu(2)
# co robi po kolei interprerter Pythona:
#   bok = 2
#   print("Rozpoczynam funkcję")
#   wynik = bok ** 2
#   # w tym momencie wiemy, że mamy zwrócić zawartość zmiennej wynik i zakończyć działanie funkcji
#   # przestają istnieć zmienne bok i wynik
#   rezultat funkcji (wartość niegdysiejszej zmiennej wynik) jest przypisywany do pole

assert pole == 4
assert pole_prostokata(2, 3) == 6
assert pole_wielu_kwadratow(2, 4) == 16

def funkcja_ktora_zwraca_liste():
    return [1, 2, 3]

def funkcja_ktora_zwraca_tuple():
    return 1, 2, 3

wynik_jak_tupla = funkcja_ktora_zwraca_tuple()
a, b, c = funkcja_ktora_zwraca_tuple()
assert a == 1
assert b == 2
assert c == 3

co_zwraca_funkcja_ktora_nic_nie_zwraca = powitaj_swiat()
assert co_zwraca_funkcja_ktora_nic_nie_zwraca == None

def powitanie_multilanguage(imie, jezyk="PL"):
    # jezyk ma wartość domyślną "PL", która zostanie użyta kiedy będzie podany tylko jeden argument
    if jezyk == "PL":
        return f"Witaj {imie}"
    elif jezyk == "EN":
        return f"Hello {imie}"

print(powitanie_multilanguage("Konrad"))  # użyta wartość domyślna jezyk, równa "PL"
print(powitanie_multilanguage("John", "EN"))

