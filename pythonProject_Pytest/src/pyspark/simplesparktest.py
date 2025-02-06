from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, to_date

spark = SparkSession.builder \
        .master("local[3]") \
        .appName("Transform2") \
        .getOrCreate()

data = [("Ram","10","8","82"),
        ("Shyam","11","12","2006"),
        ("Vinay","1","5","2"),
        ("Ram","10","8","82"),
        ("RamJr","1","28","96")]

df = spark.createDataFrame(data).toDF("name","month","day","year")

# df_parll = df.repartition(2)
#
# df.printSchema()
# df_parll.show()

#get no of partition
# print(f'no of partition: {df_parll.rdd.getNumPartitions()}')

#create a new column, use expr
df_1 = df.withColumn("year", expr("""case when year < 21 then year+1900 
                                             when year < 100 then year+2000 
                                             else year 
                                            end"""))

df_1.printSchema()
df_1.show()

df_2 = df_1.withColumn("dob", expr("to_date(concat(month,'/',day,'/',cast(year as int)),'M/d/y')"))

df_2.printSchema()
df_2.show()


df_3 = df_2.drop("day","month", "year").dropDuplicates(["name","dob"])
df_3.show()

#filter, select few columns only, take distinct
