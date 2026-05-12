# Sistema de Gestion de Viajes NYC TLC Trips 
## Descripción del Proyecto
Sistema de ingesta, procesamiento y almacenamiento de datos de viajes de taxi
y vehículos
de alquiler (FHV) de la NYC TLC. Garantiza inmutabilidad ACID y reportes
regulatorios mensuales.
## Arquitectura Seleccionada
Lakehouse con Capa Medallion (Bronze / Silver / Gold)
- Ingesta: Apache Kafka → Delta Lake (Bronze, formato Parquet)
- Procesamiento: Apache Spark → Silver (limpieza) → Gold (agregaciones)
- Servicio: Apache Druid + API Gateway + Power BI / Tableau
## Requisitos y Configuración del Entorno Técnico
| Herramienta | Versión | Propósito |
|-----------------|-----------|--------------------------------------|
| Git | 2.40+ | Control de versiones |
| Docker | 24.0+ | Contenedores de servicios |
| Python | 3.11+ | Scripts y orquestación de pipelines |
| Apache Kafka | 3.6+ | Ingesta de eventos en tiempo real |
| Apache Spark | 3.5+ | Procesamiento distribuido de datos |
| Delta Lake | 3.0+ | Almacenamiento transaccional ACID |
| PostgreSQL | 16+ | Metadatos y catálogo de datos |
| Apache Druid | 29+ | Consultas analíticas OLAP |
## Instrucciones de Instalación
# 1. Clonar el repositorio
git clone https://github.com/nyc-tlc/trips-lakehouse.git && cd trips-lakehouse
# 2. Levantar servicios (Kafka, Spark, PostgreSQL, Druid)
docker-compose up -d
# 3. Instalar dependencias Python
pip install -r requirements.txt
# 4. Inicializar esquema de metadatos
python scripts/init_db.py --env prod
# 5. Ejecutar pipeline de ingesta (Bronze layer)
python pipelines/ingest_kafka.py --topic tlc-trips --layer bronze
# 6. Ejecutar transformaciones Spark (Silver y Gold)
spark-submit pipelines/transform_silver.py && spark-submit
pipelines/transform_gold.py
## Estructura del Repositorio

nyc-tlc-lakehouse/
├── pipelines/ # Jobs Spark: ingest_kafka, transform_silver,
transform_gold
├── kafka/ # Config de topics, producers y consumers Kafka
├── schemas/ # Esquemas de datos Avro y JSON Schema
├── api/ # API Gateway con FastAPI + autenticación OAuth2
├── reports/ # Templates de reportes regulatorios Power BI
├── scripts/ # Utilidades: init_db.py, validate.py, monitor.py
├── tests/ # Pruebas unitarias e integridad de datos
├── docker-compose.yml # Orquestación de contenedores (Kafka, Spark, Druid,
PG)
├── requirements.txt # Dependencias Python (pyspark, kafka-python,
fastapi...)
└── README.md # Este archivo
