def otgan_ballar(ballar):
    natija = []
    for ball in ballar:
        if ball >= 60:
            natija.append(ball)
    return natija


assert otgan_ballar([59, 60, 75, 40]) == [60, 75]
assert otgan_ballar([60]) == [60]
assert otgan_ballar([]) == []
