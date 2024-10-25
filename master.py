import os
import sqlite3
from time import sleep
from datetime import datetime

# Inicializa la fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")

def menu(conn, cursor):
    limpiar_consola()
    print("Software de finanzas personal.\n")
    print("[1] Mostrar resumen.")
    print("[2] Añadir gastos y/o ingresos.")
    print("[3] Salir.")

    entrada = input("\n==> ")

    if entrada == "1":
        consultar_registros(cursor)
        sleep(2)
        menu(conn, cursor)  # Volver al menú después de mostrar el resumen
    elif entrada == "2":
        limpiar_consola()
        print("[+] Gastos y/o ingresos.\n")
        try:
            ingresos = float(input("Ingresos: "))
            gastos = float(input("Gastos: "))
            insertar_registro_en_db(conn, cursor, fecha_actual, ingresos, gastos)
            sleep(0.8)
            limpiar_consola()
            print("FINANZAS ACTUALIZADAS.")
            sleep(2)
            menu(conn, cursor)  # Volver al menú después de actualizar
        except ValueError:
            print("Por favor, ingresa un número válido para ingresos y gastos.")
            sleep(2)
            menu(conn, cursor)  # Volver al menú en caso de error
    elif entrada == "3":
        conn.close()
        print("Conexión cerrada. Hasta luego.")
    else:
        print("OPCIÓN DESCONOCIDA")
        sleep(2)
        menu(conn, cursor)

def init_database():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY,
        fecha TEXT,
        ganancias REAL,
        gastos REAL
    )
    ''')
    return conn, cursor  # Retornar la conexión y el cursor

def insertar_registro_en_db(conn, cursor, fecha, ganancias, gastos):
    cursor.execute("INSERT INTO registros (fecha, ganancias, gastos) VALUES (?, ?, ?)", (fecha, ganancias, gastos))
    conn.commit()  # Confirmar cambios para guardarlos de forma persistente

def consultar_registros(cursor):
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Inicializar base de datos y obtener conexión y cursor
conn, cursor = init_database()
menu(conn, cursor)
