# Interés simple
def interes_simple(P, i, n):
    return P * i * n

def monto_simple(P, i, n):
    return P + interes_simple(P, i, n)


# Interés compuesto
def monto_compuesto(P, i, n):
    return P * (1 + i) ** n

def interes_compuesto(P, i, n):
    return monto_compuesto(P, i, n) - P


# Valor presente
def valor_presente(F, i, n):
    return F / (1 + i) ** n