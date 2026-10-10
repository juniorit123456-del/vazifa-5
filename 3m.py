def elementni_ol(royxat, indeks):
    try:
        return royxat[indeks]
    except IndexError:
        return "Bunday indeks yo‘q"


assert elementni_ol([10, 20, 30], 1) == 20
assert elementni_ol([10, 20, 30], 5) == "Bunday indeks yo‘q"
