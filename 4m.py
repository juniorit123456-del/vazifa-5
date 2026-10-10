def foydalanuvchi_nomini_ol(foydalanuvchi):
    try:
        return foydalanuvchi["username"]
    except KeyError:
        return "Username topilmadi"


assert foydalanuvchi_nomini_ol({"username": "eshmat"}) == "eshmat"
assert foydalanuvchi_nomini_ol({"name": "Eshmat"}) == "Username topilmadi"
