def ballni_tekshir(ball):
    if ball < 0 or ball > 100:
        raise ValueError("Ball 0 dan 100 gacha bo‘lishi kerak")
    return ball


assert ballni_tekshir(85) == 85
assert ballni_tekshir(0) == 0
assert ballni_tekshir(100) == 100
