from pyspark.sql import SparkSession

# Configuración basada en el Artefacto 2 de tu informe
spark = SparkSession.builder \
    .appName("NYC_TLC_Lakehouse_Ingest") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .getOrCreate()

print(">>> Iniciando Ingesta desde Apache Kafka...")
# Aquí se conectaría al bus de mensajes tolerante a fallos
print(">>> Almacenando datos en Delta Lake (Capa Bronze - Inmutable)...")
