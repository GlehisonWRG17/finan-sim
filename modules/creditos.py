import pandas as pd

def cuota_frances(P, i, n):
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1)

def tabla_amortizacion(P, i, n):
    cuota = cuota_frances(P, i, n)
    saldo = P

    datos = []

    for periodo in range(1, int(n)+1):
        interes = saldo * i
        capital = cuota - interes
        saldo -= capital

        datos.append([
            periodo,
            cuota,
            interes,
            capital,
            saldo
        ])

    df = pd.DataFrame(datos, columns=[
        "Periodo",
        "Cuota",
        "Interés",
        "Capital",
        "Saldo"
    ])

    return df