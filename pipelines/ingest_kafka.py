# Script para Hito H2: Ingesta Bronze
from pyspark.sql import SparkSession

def iniciar_ingesta():
    spark = SparkSession.builder \
        .appName("NYC_TLC_Bronze_Ingestion") \
        .getOrCreate()

    # Simulando la lectura del dataset de la TLC
    print("Conectando a tópico Kafka: nyc-trips...")
    print("Guardando datos en formato Delta (Capa Bronze)...")

    # Aquí iría la lógica de lectura de Kafka que pusiste en el informe
    # spark.readStream.format("kafka")...
    
if __name__ == "__main__":
    iniciar_ingesta()