

def grade(qz: int, fn: int, pj: int, ex: int, rd: int) -> int:
    final: int = round((qz * 30.0 + fn * 20.0 + pj * 15.0 + ex * 20.0 + rd * 15.0) / 100)
    return final

print(grade(95, 95, 32, 95, 95))