import math
def calculo_distancia(Ax, Ay, Bx, By):
    return math.sqrt((Bx - Ax)**2 + (By - Ay)**2)
def autonomia(carga, distancia):
    if carga <= 50000:
        autonomia_base = 18000
    elif 50001 <= carga <= 200000:
        autonomia_base = 9000
    elif 200000 <= carga <=250000:
        autonomia_base = 3000
    autonomia_adicional = autonomia_base * 0.1
    autonomia_total = autonomia_base + autonomia_adicional
    if distancia <= autonomia_base:
        return "SIM"
    elif autonomia_base <= distancia <= autonomia_total:
        return "TALVEZ"
    else:
        return "NAO"
def main():
    carga = float(input())
    Ax = float(input())
    Ay = float(input())
    Bx = float(input())
    By = float(input())
    distancia = calculo_distancia(Ax, Ay, Bx, By)
    print(f"{distancia:.2f}")
    print(f"{autonomia(carga, distancia)}")
main()