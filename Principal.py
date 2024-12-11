import requests
import sqlite3
import matplotlib.pyplot as plt
import datetime

# Configuración de la API
CLAVE_API = "31d47cf6910b595c9fffe56a6a652c3a"
URL_BASE = "http://api.marketstack.com/v1/"

# Crea la base de datos y la tabla si no existen.
def crear_base_de_datos():
    conexion = sqlite3.connect("datos_mercado.db")
    cursor = conexion.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS datos_mercado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            fecha TEXT,
            apertura REAL,
            maximo REAL,
            minimo REAL,
            cierre REAL,
            volumen INTEGER
        )
    ''')
    conexion.commit()
    conexion.close()

# Obtiene datos de la API de MarketStack.
def obtener_datos_de_api(ticker, fecha_inicio, fecha_fin):
    endpoint = f"{URL_BASE}eod"
    parametros = {
        "access_key": CLAVE_API,
        "symbols": ticker,
        "date_from": fecha_inicio,
        "date_to": fecha_fin
    }
    respuesta = requests.get(endpoint, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos.get("data", [])
    else:
        print("Error al conectar con la API:", respuesta.status_code, respuesta.text)
        return []

# Guarda los datos en la base de datos SQLite.
def guardar_datos_en_base(ticker, datos):
    conexion = sqlite3.connect("datos_mercado.db")
    cursor = conexion.cursor()
    for entrada in datos:
        cursor.execute('''
            INSERT INTO datos_mercado (ticker, fecha, apertura, maximo, minimo, cierre, volumen)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ticker, entrada["date"], entrada["open"], entrada["high"], entrada["low"], entrada["close"], entrada["volume"]))
    conexion.commit()
    conexion.close()

# Muestra un resumen de los tickers y rangos de fechas en la base de datos.
def mostrar_resumen():
    conexion = sqlite3.connect("datos_mercado.db")
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT ticker, MIN(fecha), MAX(fecha) FROM datos_mercado
        GROUP BY ticker
    ''')
    filas = cursor.fetchall()
    conexion.close()

    if filas:
        print("Los tickers guardados en la base de datos son:")
        for fila in filas:
            print(f"{fila[0]} - {fila[1]} <-> {fila[2]}")
    else:
        print("No hay datos almacenados en la base de datos.")

# Genera un gráfico de los datos de un ticker almacenado.
def graficar_datos_ticker(ticker):
    conexion = sqlite3.connect("datos_mercado.db")
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT fecha, cierre FROM datos_mercado
        WHERE ticker = ?
        ORDER BY fecha
    ''', (ticker,))
    filas = cursor.fetchall()
    conexion.close()

    if filas:
        fechas = [datetime.datetime.strptime(fila[0].split("T")[0], "%Y-%m-%d") for fila in filas]
        cierres = [fila[1] for fila in filas]

        plt.figure(figsize=(10, 5))
        plt.plot(fechas, cierres, marker="o", label=f"Precio de cierre: {ticker}")
        plt.title(f"Precio de cierre para {ticker}")
        plt.xlabel("Fecha")
        plt.ylabel("Precio de cierre")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print(f"No hay datos almacenados para el ticker {ticker}.")

# Menú principal del programa.
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Actualización de datos")
        print("2. Visualización de datos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ticker = input("Ingrese el ticker a pedir: ").upper()
            fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese fecha de fin (YYYY-MM-DD): ")
            print("Pidiendo datos ...")
            datos = obtener_datos_de_api(ticker, fecha_inicio, fecha_fin)
            if datos:
                guardar_datos_en_base(ticker, datos)
                print("Datos guardados correctamente.")
            else:
                print("No se obtuvieron datos de la API.")
        elif opcion == "2":
            print("\n--- Visualización de datos ---")
            print("1. Resumen")
            print("2. Gráfico de ticker")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                mostrar_resumen()
            elif sub_opcion == "2":
                ticker = input("Ingrese el ticker a graficar: ").upper()
                graficar_datos_ticker(ticker)
            else:
                print("Opción no válida.")
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    crear_base_de_datos()
    menu_principal()