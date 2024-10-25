import os
import sqlite3
from time import sleep
from datetime import datetime

def init_database():
    """Inicializa la base de datos y devuelve la conexión y el cursor."""
    conn = sqlite3.connect('mi_base_de_datos.db')  # Usa una ruta absoluta si es necesario
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY,
        fecha TEXT,
        ganancias REAL,
        gastos REAL
    )
    ''')
    return conn, cursor

def insertar_registro_en_db(cursor, fecha, ganancias, gastos):
    """Inserta un nuevo registro de ingresos y gastos en la base de datos."""
    cursor.execute("INSERT INTO registros (fecha, ganancias, gastos) VALUES (?, ?, ?)", (fecha, ganancias, gastos))

def consultar_registros(cursor):
    """Consulta y muestra todos los registros de la base de datos."""
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def menu(conn, cursor):
    """Muestra el menú principal y gestiona las opciones."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Software de finanzas personal.\n")
        print("[1] Mostrar resumen.")
        print("[2] Añadir gastos y/o ingresos.")
        print("[0] Salir.")
        
        entrada = input("\n==> ")

        if entrada == "1":
            consultar_registros(cursor)
            sleep(2)
        elif entrada == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[+] Gastos y/o ingresos.\n")
            try:
                ingresos = float(input("Ingresos: "))
                gastos = float(input("Gastos: "))
                fecha_actual = datetime.now().strftime("%Y-%m-%d")
                insertar_registro_en_db(cursor, fecha_actual, ingresos, gastos)
                conn.commit()  # Asegúrate de hacer commit después de la inserción
                sleep(2)
                print("FINANZAS ACTUALIZADAS.")
                sleep(2)
            except ValueError:
                print("Por favor, ingresa un número válido para ingresos y gastos.")
                sleep(2)
        elif entrada == "0":
            break
        else:
            print("OPCION DESCONOCIDA")
            sleep(2)

if __name__ == "__main__":
    # Inicializar base de datos y obtener conexión y cursor
    conn, cursor = init_database()
    menu(conn, cursor)
    conn.close()  # Cerrar la conexión al final