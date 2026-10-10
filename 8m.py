def narxlar(narx_matnlari):
    narxlar = []
    for matn in narx_matnlari:
        try:
            narx = int(matn)
            narxlar.append(narx)
        except ValueError:
            print("Noto‘g‘ri narx:", matn)
    return narxlar


assert narxlar(["12000", "x", "5000"]) == [12000, 5000]
assert narxlar([]) == []
