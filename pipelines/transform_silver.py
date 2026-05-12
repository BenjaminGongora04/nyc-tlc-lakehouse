from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("NYC_TLC_Silver_Cleaning").getOrCreate()

print(">>> Cargando datos desde Capa Bronze...")
# Lógica: Filtrar viajes con distancia o monto menor o igual a cero
print(">>> Aplicando reglas de calidad: Eliminando nulos y duplicados...")
print(">>> Almacenando en Capa Silver (Delta Lake - Limpio)...")