# Comentário para modificar o arquivo .py
import pyspark.sql.functions as F
from pyspark.sql import SparkSession   # Done automatically at Notebook, but here it's necessary

spark = (
    SparkSession
    .builder
    .appName("ExerciseSpark")
    .getOrCreate()
)


# Ler os dados do enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-manoel-385970729661/raw-data/enem/")
)


# Export in parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-manoel-385970729661/staging/enem")
)