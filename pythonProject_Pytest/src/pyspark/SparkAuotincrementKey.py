import random
from datetime import datetime, timedelta

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, monotonically_increasing_id, udf, to_date, date_format, col, when
from pyspark.sql import functions as f
from pyspark.sql.types import DateType, StructField, StructType, IntegerType, FloatType

from lib.logger import Log4j

spark = SparkSession.builder \
       .master("local[3]") \
       .appName("SparkAutoIncrementKey") \
       .getOrCreate()


logger = Log4j(spark)

logger.info("AutoIncrement key code start:")

read_df = spark.read.format("csv") \
         .option("header", "true") \
         .option("inferschema", "true") \
         .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\SOCR-HeightWeight.csv")

read_df.show(5)
logger.info("schema: " + read_df.schema.simpleString())

#read heieghtweight.csv, rename column appropriately,
#add a new column with height in feet
# ADD unique key montonosely generating,

read_df_transformed = read_df.withColumnRenamed("Height(Inches)", "Height_Inch") \
      .withColumnRenamed("Weight(Pounds)", "Weight_Pound") \
      .withColumn("Height_Ft", f.round(expr("`Height_Inch`/12"),2)) \
     .withColumn("Customer_key",monotonically_increasing_id())

read_df_transformed.show(5)


# add a date coulmn to this df using random module
#create a udf and register it and use it to generate random date
def generate_random_date():
    start_date = datetime(2020,1,1)
    end_date = datetime(2024,12,31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date+timedelta(days=random_days)

#register the udf for dataframe
random_Date_udf = udf(generate_random_date, DateType())
read_df_transformed_2 = read_df_transformed.withColumn("Capture_Date", random_Date_udf())

read_df_transformed_2.show(5)


#provide explicit schema to this csv
Height_weight_schema = StructType([StructField("RowNum", IntegerType()),
           StructField("Height_Inch", FloatType()),
           StructField("weight_pound", FloatType()),
           StructField("Height_Feet",FloatType()),
           StructField("customer_key",IntegerType()),
           StructField("capture_date",DateType())
           ])


read_explicit_schema_df = spark.read.format("csv") \
                        .option("header","true") \
                        .schema(Height_weight_schema) \
                        .load("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\SOCR-HeightWeight.csv")

read_explicit_schema_df.show(5)

# and an a different new explicity date format

final_df = read_df_transformed_2.withColumn("Capture_Date_Fmt",date_format("Capture_Date",'yyyy/M/d'))
final_df.show(5)



#test repartition


#find records where a column "height" value is null
#filter them out
#find group by weight round up to 0 decimal place, how many folks are there in range of 100-150
final_df.filter(col("Height_Inch").isNotNull()) \
        .select(
             when((col("Weight_Pound").cast("float")>100) & (col("Weight_Pound").cast("float")<=150), "100-150")
             .when((col("Weight_Pound").cast("float")>150) & (col("Weight_Pound").cast("float")<=200), "150-200")
             .when((col("Weight_Pound").cast("float")>200) & (col("Weight_Pound").cast("float")<=250), "200-250")
             .alias("Weight_range")
          ) \
        .groupby("Weight_range") \
        .count() \
        .show()


#also experiment with repartition
#this i have not done now. will plan next

#create dataframe or order type, with sample rows and do group by operation
# how many orders in a day or from one given zip
data_1 = [('anil','5000','Rice','Bangalore'),
          ('Ashok','4000','Pulse', 'Patna'),
          ('Avinash','6000','Makhana','Patna'),
          ('Sunil','2000','Almond','Bangalore'),
          ('kamal','1000','Aata','Deoghar')]

df_2 = spark.createDataFrame(data_1).toDF("cutomer_name","order_amount","Item_Name","Location")
df_3= df_2.withColumn("order_id", monotonically_increasing_id())

# how many orders from one given zip
#group by location, count of order
df_3.filter(col("order_amount")>1000)\
    .groupby("Location") \
    .count().alias("Count_Of_Orders") \
    .orderBy("Location") \
    .show()

