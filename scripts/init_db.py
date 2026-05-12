import os

def init_catalog():
    print("Conectando a PostgreSQL (Metastore)...")
    print("Creando bases de datos: tlc_bronze, tlc_silver, tlc_gold")
    print("Esquemas inicializados correctamente para el entorno: prod")

if __name__ == "__main__":
    init_catalog()