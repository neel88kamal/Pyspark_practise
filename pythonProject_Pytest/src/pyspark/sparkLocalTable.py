from pyspark.sql import *
from lib.logger import Log4j

spark1 = SparkSession.builder\
       .appName("SparkLocalTable") \
       .master("local[3]") \
       .config("spark.sql.catalogImplementation", "in-memory") \
       .getOrCreate()

logger = Log4j(spark1)

parquetsparkdf = spark1.read \
                .format("parquet") \
                .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\data\\flight-time.parquet")

parquetsparkdf.show(5)

spark1.sql("create database if not exists airline_db")
spark1.catalog.setCurrentDatabase('airline_db')

parquetsparkdf.write.mode("overwrite").saveAsTable("flight_data_tbl")

logger.info(spark1.catalog.listTables('airline_db'))


