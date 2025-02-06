from Tools.demo.sortvisu import distinct
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
        .master("local[3]") \
        .appName("sparktransform1") \
        .getOrCreate()

print(spark.sparkContext.uiWebUrl)

readcsvdf = spark.read \
    .format("csv") \
    .option("header","true") \
    .option("inferSchema","true") \
    .option("encoding", "UTF-16") \
    .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\new_fire_dpt.csv")


# readcsvdf.show(5, truncate=False)


readcsvdf_rename = readcsvdf.withColumnRenamed("Call Type","call_type") \
         .withColumnRenamed("Zipcode of Incident", "zip_incident") \
         .withColumnRenamed("Call Date","call_date")

# print(readcsvdf_new.columns)

readcsvdf_new = readcsvdf_rename.repartition(2)

# readcsvdf_new.select('call_type') \
#               .filter(col('call_type').isNotNull()) \
#              .distinct() \
#              .show()
#
# print(readcsvdf_new.select('call_type') \
#             .distinct() \
#             .count())

readcsvdf_new.select('call_type') \
            .where('call_type is not null') \
            .groupby('call_type') \
            .count() \
            .orderBy("count", ascending=False) \
            .show()
input("enter value")




