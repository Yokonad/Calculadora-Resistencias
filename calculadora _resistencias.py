import math
import os
import time

COLORES = [
    ("Negro", 0, None, None),
    ("Marron", 1, 1, 100),
    ("Rojo", 2, 2, 50),
    ("Naranja", 3, None, 15),
    ("Amarillo", 4, None, 25),
    ("Verde", 5, 0.5, None),
    ("Azul", 6, 0.25, 10),
    ("Violeta", 7, 0.1, 5),
    ("Gris", 8, 0.05, None),
    ("Blanco", 9, None, None),
    ("Dorado", None, 5, None),
    ("Plateado", None, 10, None)
]

VALORES_COMERCIALES = [
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
    10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91,
    100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910,
    1000, 1100, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600, 3900, 4300, 4700, 5100, 5600, 6200, 6800, 7500, 8200, 9100,
    10000, 11000, 12000, 13000, 15000, 16000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 36000, 39000, 43000, 47000, 51000, 56000, 62000, 68000, 75000, 82000, 91000,
    100000, 110000, 120000, 130000, 150000, 160000, 180000, 200000, 220000, 240000, 270000, 300000, 330000, 360000, 390000, 430000, 470000, 510000, 560000, 620000, 680000, 750000, 820000, 910000,
    1000000
]

historial = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    print("CALCULADORA DE RESISTENCIAS POR CODIGO DE COLORES")
    print("Version 2.0 - Herramienta Profesional")
    print("=" * 50)
    print()

def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print("-" * 20)
    print("1. Calcular resistencia por colores")
    print("2. Historial de calculos")
    print("3. Ayuda y guia de uso")
    print("4. Salir")
    print()

def mostrar_ayuda():
    print("GUIA DE AYUDA")
    print("=" * 50)
    print()
    print("LECTURA DE RESISTENCIAS:")
    print("  - Las resistencias tienen 4, 5 o 6 bandas de colores")
    print("  - Se leen de izquierda a derecha")
    print("  - La banda mas ancha o separada es la de tolerancia")
    print()
    print("TIPOS DE RESISTENCIAS:")
    print("  - 4 bandas: 2 digitos + multiplicador + tolerancia")
    print("  - 5 bandas: 3 digitos + multiplicador + tolerancia")
    print("  - 6 bandas: 3 digitos + multiplicador + tolerancia + coef. termico")
    print()
    print("UNIDADES:")
    print("  - Ohm (Ohmios), kOhm (Kiloohmios), MOhm (Megaohmios), GOhm (Gigaohmios)")
    print("  - 1 kOhm = 1,000 Ohm")
    print("  - 1 MOhm = 1,000,000 Ohm")
    print()
    print("TOLERANCIA:")
    print("  - Indica la precision de la resistencia")
    print("  - ±5% es estandar, ±1% es alta precision")
    print()
    print("TABLA DE COLORES:")
    print("  Negro=0, Marron=1, Rojo=2, Naranja=3, Amarillo=4")
    print("  Verde=5, Azul=6, Violeta=7, Gris=8, Blanco=9")
    print("  Dorado=±5%, Plateado=±10%")
    print()
    input("Presiona Enter para continuar...")

def mostrar_colores(indices, tipo_banda=None):
    print("SELECCION DE COLOR - " + (tipo_banda.upper() if tipo_banda else "COLORES"))
    print("-" * 30)
    
    for i in indices:
        nombre = COLORES[i][0]
        
        if tipo_banda == "digito":
            extra = f" (valor: {COLORES[i][1]})"
        elif tipo_banda == "multiplicador":
            if nombre == "Dorado":
                extra = " (x0.1)"
            elif nombre == "Plateado":
                extra = " (x0.01)"
            else:
                extra = f" (x10^{COLORES[i][1]})"
        elif tipo_banda == "tolerancia":
            extra = f" (±{COLORES[i][2]}%)"
        elif tipo_banda == "temp":
            extra = f" ({COLORES[i][3]} ppm/C)" if COLORES[i][3] else ""
        else:
            extra = ""
        
        print(f"{i:2}. {nombre:9}{extra}")
    
    print()

def pedir_color(indices, mensaje, tipo_banda=None):
    while True:
        mostrar_colores(indices, tipo_banda)
        try:
            idx = int(input(mensaje))
            if idx in indices:
                return idx
        except ValueError:
            pass
        print("Opcion invalida. Intenta de nuevo.")
        time.sleep(1)
        limpiar_pantalla()
        mostrar_banner()

def mostrar_historial():
    print("HISTORIAL DE CALCULOS")
    print("=" * 50)
    print()
    
    if not historial:
        print("No hay calculos en el historial.")
    else:
        for i, calculo in enumerate(historial[-10:], 1):
            print(f"{i:2}. {calculo['valor']} (±{calculo['tolerancia']}%) - {calculo['timestamp']}")
    
    print()
    input("Presiona Enter para continuar...")

def agregar_al_historial(valor, tolerancia):
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    historial.append({
        'valor': formatear_valor(valor),
        'tolerancia': tolerancia,
        'timestamp': timestamp
    })

def valor_resistencia(bandas, seleccion):
    if bandas == 4:
        d1, d2, mul, tol = seleccion
        if COLORES[mul][0] == "Dorado":
            valor = (COLORES[d1][1]*10 + COLORES[d2][1]) * 0.1
        elif COLORES[mul][0] == "Plateado":
            valor = (COLORES[d1][1]*10 + COLORES[d2][1]) * 0.01
        else:
            valor = (COLORES[d1][1]*10 + COLORES[d2][1]) * (10 ** COLORES[mul][1])
        tolerancia = COLORES[tol][2]
        return valor, tolerancia, None
    elif bandas == 5 or bandas == 6:
        d1, d2, d3, mul, tol = seleccion[:5]
        if COLORES[mul][0] == "Dorado":
            valor = (COLORES[d1][1]*100 + COLORES[d2][1]*10 + COLORES[d3][1]) * 0.1
        elif COLORES[mul][0] == "Plateado":
            valor = (COLORES[d1][1]*100 + COLORES[d2][1]*10 + COLORES[d3][1]) * 0.01
        else:
            valor = (COLORES[d1][1]*100 + COLORES[d2][1]*10 + COLORES[d3][1]) * (10 ** COLORES[mul][1])
        tolerancia = COLORES[tol][2]
        coef_temp = None
        if bandas == 6:
            temp_idx = seleccion[5]
            coef_temp = COLORES[temp_idx][3]
        return valor, tolerancia, coef_temp
    else:
        return None, None, None

def formatear_valor(valor):
    if valor >= 1e9:
        return f"{valor/1e9:.2f} GΩ"
    elif valor >= 1e6:
        return f"{valor/1e6:.2f} MΩ"
    elif valor >= 1e3:
        return f"{valor/1e3:.2f} kΩ"
    else:
        return f"{valor:.2f} Ω"

def valores_comerciales_cercanos(valor, n=3):
    valor_k = valor / 1000
    ordenados = sorted(VALORES_COMERCIALES, key=lambda x: abs(x - valor_k))
    return [(v*1000, abs(v*1000 - valor)) for v in ordenados[:n]]

def sugerir_combinaciones_paralelo(valor):
    mejor = None
    error_min = float('inf')
    valores = VALORES_COMERCIALES[:50]
    for i, r1 in enumerate(valores):
        for r2 in valores[i:]:
            rp = 1 / (1/(r1*1000) + 1/(r2*1000))
            error = abs(rp - valor)
            error_p = (error / valor) * 100
            if error < error_min and error_p < 20:
                error_min = error
                mejor = (r1*1000, r2*1000, rp, error_p)
    return mejor

def sugerir_combinaciones_serie(valor):
    mejor = None
    error_min = float('inf')
    valores = VALORES_COMERCIALES[:40]
    for i, r1 in enumerate(valores):
        for r2 in valores[i:]:
            rs = r1*1000 + r2*1000
            error = abs(rs - valor)
            error_p = (error / valor) * 100
            if error < error_min and error_p < 20:
                error_min = error
                mejor = (r1*1000, r2*1000, rs, error_p)
    return mejor

def calcular_resistencia_principal():
    print("CALCULO POR CODIGO DE COLORES")
    print("=" * 50)
    print()
    
    while True:
        try:
            bandas = int(input("¿Cuantas bandas tiene la resistencia? (4, 5 o 6): "))
            if bandas in (4, 5, 6):
                break
        except ValueError:
            pass
        print("Por favor, ingresa 4, 5 o 6.")

    seleccion = []
    if bandas == 4:
        print("\nConfigurando resistencia de 4 bandas...")
        d1 = pedir_color(range(1,10), "Selecciona el color de la 1a banda (digito 1): ", "digito")
        d2 = pedir_color(range(0,10), "Selecciona el color de la 2a banda (digito 2): ", "digito")
        mul = pedir_color(range(0,12), "Selecciona el color de la 3a banda (multiplicador): ", "multiplicador")
        tol = pedir_color([1,2,5,6,10,11], "Selecciona el color de la 4a banda (tolerancia): ", "tolerancia")
        seleccion = (d1, d2, mul, tol)
    elif bandas == 5:
        print("\nConfigurando resistencia de 5 bandas...")
        d1 = pedir_color(range(1,10), "Selecciona el color de la 1a banda (digito 1): ", "digito")
        d2 = pedir_color(range(0,10), "Selecciona el color de la 2a banda (digito 2): ", "digito")
        d3 = pedir_color(range(0,10), "Selecciona el color de la 3a banda (digito 3): ", "digito")
        mul = pedir_color(range(0,12), "Selecciona el color de la 4a banda (multiplicador): ", "multiplicador")
        tol = pedir_color([1,2,5,6,10,11], "Selecciona el color de la 5a banda (tolerancia): ", "tolerancia")
        seleccion = (d1, d2, d3, mul, tol)
    elif bandas == 6:
        print("\nConfigurando resistencia de 6 bandas...")
        d1 = pedir_color(range(1,10), "Selecciona el color de la 1a banda (digito 1): ", "digito")
        d2 = pedir_color(range(0,10), "Selecciona el color de la 2a banda (digito 2): ", "digito")
        d3 = pedir_color(range(0,10), "Selecciona el color de la 3a banda (digito 3): ", "digito")
        mul = pedir_color(range(0,12), "Selecciona el color de la 4a banda (multiplicador): ", "multiplicador")
        tol = pedir_color([1,2,5,6,10,11], "Selecciona el color de la 5a banda (tolerancia): ", "tolerancia")
        temp = pedir_color([1,2,3,4,6,7], "Selecciona el color de la 6a banda (coeficiente termico): ", "temp")
        seleccion = (d1, d2, d3, mul, tol, temp)

    valor, tolerancia, coef_temp = valor_resistencia(bandas, seleccion)
    if valor is None:
        print("Error en la seleccion de bandas.")
        return

    print("\nRESULTADOS")
    print("=" * 20)
    print(f"Valor calculado: {formatear_valor(valor)}")
    print(f"Tolerancia: ±{tolerancia}%")
    if coef_temp:
        print(f"Coeficiente termico: {coef_temp} ppm/C")
    
    valor_min = valor * (1 - tolerancia/100)
    valor_max = valor * (1 + tolerancia/100)
    print(f"Rango posible: {formatear_valor(valor_min)} - {formatear_valor(valor_max)}")

    print("\nValores comerciales cercanos:")
    for v, error in valores_comerciales_cercanos(valor, 3):
        print(f"  {formatear_valor(v)} (error: {error/valor*100:.1f}%)")

    paralelo = sugerir_combinaciones_paralelo(valor)
    if paralelo:
        r1, r2, rp, error_p = paralelo
        print(f"\nAlternativa en paralelo: {formatear_valor(r1)} || {formatear_valor(r2)} = {formatear_valor(rp)} (error: {error_p:.1f}%)")

    serie = sugerir_combinaciones_serie(valor)
    if serie:
        r1, r2, rs, error_s = serie
        print(f"Alternativa en serie: {formatear_valor(r1)} + {formatear_valor(r2)} = {formatear_valor(rs)} (error: {error_s:.1f}%)")

    agregar_al_historial(valor, tolerancia)
    
    print("\nCalculo completado!")
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu_principal()
        
        try:
            opcion = int(input("Selecciona una opcion (1-4): "))
            
            if opcion == 1:
                limpiar_pantalla()
                mostrar_banner()
                calcular_resistencia_principal()
            elif opcion == 2:
                limpiar_pantalla()
                mostrar_banner()
                mostrar_historial()
            elif opcion == 3:
                limpiar_pantalla()
                mostrar_banner()
                mostrar_ayuda()
            elif opcion == 4:
                print("\nGracias por usar la Calculadora de Resistencias!")
                print("Desarrollado para facilitar el trabajo con componentes electronicos.")
                break
            else:
                print("Opcion invalida. Selecciona un numero del 1 al 4.")
                time.sleep(1)
                
        except ValueError:
            print("Por favor, ingresa un numero valido.")
            time.sleep(1)

if __name__ == "__main__":
    main()
