def ballni_ol(matn):
    try:
        ball = int(matn)
    except ValueError:
        return "Ball son bo‘lishi kerak"
    return ball


assert ballni_ol("85") == 85
assert ballni_ol("sakson") == "Ball son bo‘lishi kerak"
