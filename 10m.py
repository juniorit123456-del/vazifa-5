def chegirmali_narxlar(narx_matnlari, chegara):
    if chegara < 0:
        raise ValueError("Chegara manfiy bo‘lishi mumkin emas")

    natija = []
    for matn in narx_matnlari:
        try:
            narx = int(matn)
        except ValueError:
            continue
        if narx >= chegara:
            natija.append(narx - 2000)
    return natija


assert chegirmali_narxlar(["9000", "10000", "15000", "x"], 10000) == [8000, 13000]
assert chegirmali_narxlar([], 10000) == []
assert chegirmali_narxlar(["12000"], 0) == [10000]
