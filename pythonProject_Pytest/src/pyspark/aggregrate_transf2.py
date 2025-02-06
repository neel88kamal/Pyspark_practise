from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.functions import expr, weekofyear, to_timestamp, col

spark = SparkSession.builder \
        .master("local[3]") \
        .appName("aggtest1") \
        .getOrCreate()

dfagg = spark.read \
        .format('csv') \
        .option("header","true") \
        .option("inferSchema", "true") \
        .load('../../data/invoices.csv')

dfagg.printSchema()
dfagg.show(5)

dfagg_d = dfagg.withColumn("InvoiceDate", expr("to_date(substring(InvoiceDate,1,10),'dd-MM-yyyy')"))
dfagg_d.printSchema()
dfagg_d.show(5)

#show total invoice count and total quantity, avg price
dfagg_d.agg(f.count("InvoiceNo").alias("Total_Invoice_count"),
            f.sum("Quantity").alias("Total_Quantity"),
            f.round(f.avg(expr("Quantity * UnitPrice")),2).alias("Avg_Price") ).show()

#can also be done like below

dfagg_d.select(f.count("InvoiceNo").alias("Total_Invoice_count"),
            f.sum("Quantity").alias("Total_Quantity"),
            f.round(f.avg(expr("Quantity * UnitPrice")),2).alias("Avg_Price") ).show()

# question -> df that aggregates to show following,
# group it by country and weeknumber (derive it from invoice date),
# and find number of unique invoices, totalquantity, totalinvoice value

df_final = dfagg_d.groupby("Country",weekofyear("InvoiceDate").alias("WeekOfYear")) \
            .agg(f.countDistinct("InvoiceNo").alias("NumInvoices"),
               f.sum("Quantity").alias("TotalQuantity"),
               f.round(f.sum(expr("Cast(Quantity as INT)") * col("UnitPrice")),2).alias("InvoiceValue")) \
            .orderBy("Country")

df_final.show(10)

# df= dfagg \
#     .groupby("Country", weekofyear("InvoiceDate")) \
#     .agg(f.countDistinct("InvoiceNo").alias("UniqueInvoices"),
#          f.sum("Quantity").alias("totalquantity"),
#          f.round(f.sum(expr("Quantity * UnitPrice")),2).alias("totalinvoice")
#          )



#show total invoice count and total quantity, avg price
#do it using spark sql and spark df method
#
# #sparksql method
# dfagg.createOrReplaceTempView('sales')
# summary_sql = spark.sql("""
#               select count(cast(InvoiceNo as int)), sum(Quantity),
#               round(avg(UnitPrice),2)
#               from sales
#               """)
# summary_sql.show()
#
# #df method
# dfagg.select(f.count("*").alias("total_count"),
#              f.sum("Quantity").alias("TotalQuantity"),
#              f.round(f.avg("UnitPrice"),2).alias("AvgPrice")
#              ).show()


# question -> df that aggregates to show following, group it by country and weeknumber (derive it from invoice date), and find number of unique invoices, totalquantity, totalinvoice value

# dfagg = dfagg.withColumn("InvoiceDate", to_timestamp("InvoiceDate", "dd-MM-yyyy H.mm"))
# dfagg.show(5)
#
#
# df= dfagg \
#     .groupby("Country", weekofyear("InvoiceDate")) \
#     .agg(f.countDistinct("InvoiceNo").alias("UniqueInvoices"),
#          f.sum("Quantity").alias("totalquantity"),
#          f.round(f.sum(expr("Quantity * UnitPrice")),2).alias("totalinvoice")
#          )
#
# df.show()