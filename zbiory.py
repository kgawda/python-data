zbior = {"pies", "kot"}
print(zbior)

assert len(zbior) == 2
assert "kot" in zbior  # to działa bardzo wydajnie

zbior.add("chomik")
assert len(zbior) == 3

zbior.remove("kot")
assert "kot" not in zbior

# bez powtórzeń
zbior.add("pies")
zbior.add("pies")
assert len(zbior) == 2

zbior2 = set(["kakadu", "ara"])

for zwierzak in zbior:
    print(zwierzak)

ssaki = {"kot", "pies", "nietoperz"}
latajace = {"papuga", "nietoperz"}
# część wspólna:
assert ssaki & latajace == {'nietoperz'}
# suma:
assert ssaki | latajace == {'pies', 'kot', 'papuga', 'nietoperz'}  # trick: to działa też dla dict
# różnica:
assert ssaki - latajace == {'kot', 'pies'}
# część rozłączna
assert ssaki ^ latajace == {'kot', 'pies', 'papuga'}
# Uwaga: wszystkie te operacje tworzą nowy zbiór. Nie modyfikują ani zbioru ssaki ani latajace

pusty_zbior = set()
assert len(pusty_zbior) == 0

# Nie-mutowalna wersja set:
frozenset(zbior)
frozenset([1, 2, 3])
