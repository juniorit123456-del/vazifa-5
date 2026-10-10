def xavfsiz_bolish(a, b):
    if b == 0:
        return "0 ga bo‘lish mumkin emas"
    return a / b


assert xavfsiz_bolish(12, 3) == 4.0
assert xavfsiz_bolish(12, 0) == "0 ga bo‘lish mumkin emas"
