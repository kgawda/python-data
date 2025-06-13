import random

sekret = random.randint(1, 100)
zgadl = False

for numer_proby in range(1, 6):
    # print("To twoja", numer_proby, "proba.")
    strzal = input("Podaj liczbę: ")
    try:
        strzal = int(strzal)
    except ValueError:
        print("To nie jest liczba")
        break  # kończymy zabawę
    # else:  # jeżeli nie wystąpił żaden błąd
    #     print("Podałeś liczbę", strzal)
    if strzal == sekret:
        print("BRAWO!")
        break
    elif strzal < sekret:
        print("Sekretna liczba jest większa")
    else:
        print("Sekretna liczba jest mniejsza")

if not zgadl:
    print(f"Nie udało się. Sekretna liczba to: {sekret}")
