# Conversión de tasa nominal a efectiva
def nominal_a_efectiva(i_nominal, m):
    return (1 + i_nominal / m) ** m - 1

# Conversión de tasa efectiva a nominal
def efectiva_a_nominal(i_efectiva, m):
    return m * ((1 + i_efectiva) ** (1/m) - 1)

# Conversión entre tasas efectivas de distintos periodos
def convertir_efectiva(i_origen, n_origen, n_destino):
    return (1 + i_origen) ** (n_origen / n_destino) - 1

def porcentaje(valor):
    return valor * 100

def decimal(valor):
    return valor / 100