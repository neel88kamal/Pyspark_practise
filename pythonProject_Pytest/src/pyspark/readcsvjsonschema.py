from pyspark.sql import SparkSession

from lib.logger import Log4j

spark = SparkSession.builder\
        .master("local[3]") \
        .appName("readcsvjson") \
        .getOrCreate()

logger = Log4j(spark)

fire_df = spark.read.format("csv") \
            .option("header","true") \
            .option("inferschema","true") \
            .option("encoding", "UTF-16") \
            .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\new_fire_dpt.csv")

fire_df.printSchema()
fire_df.show(5)
#how to check if default infer schema is correct

flight_csv_df= spark.read.format("csv") \
                .option("header","true") \
                .load("C:\\Users\\neelk\PycharmProjects\\pythonProject_Pytest\\data\\flight-time.csv")

logger.info(flight_csv_df.schema.simpleString())


flight_json_df = spark.read.format("json") \
                .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\flight-time.json")

logger.info("JSON schema:" + flight_json_df.schema.simpleString())


#how to explicitly associate a schema



#how to create a dataframe using structtype, structfield
#hot to create a dataframe using df.createdataframe.todf