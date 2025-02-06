from pyspark.shell import spark
from pyspark.sql.functions import *
from pyspark.sql.types import *

def to_date_df(df, fmt, field):
    return df.withColumn(field, to_date(col(field),fmt))


#schema
my_schema = StructType([
    StructField("ID", StringType()),
    StructField("EventDate",StringType()) ])

#row
my_row = [Row("123","04/05/2020"), Row("124","05/06/2021")]

my_rdd = spark.sparkContext.parallelize(my_row,2)
my_df = spark.createDataFrame(my_rdd, my_schema)

my_df.printSchema()
my_df.show()
new_df = to_date_df(my_df, "M/d/y", "EventDate")
new_df.printSchema()
new_df.show()
