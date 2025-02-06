import configparser

from pyspark import SparkConf

def get_spark_conf():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key,val)
    return spark_conf


def load_source_read_df(sparkcontext):
    return sparkcontext.read \
                .option("header", "true") \
                .option("inferschema", "true") \
                .csv("C:\\Users\\neelk\\PycharmProjects\\pythonProject_Pytest\\data\\sample.csv")

def count_by_country_df(df):
    return df.select("Age", "Gender", "Country", "state") \
             .filter("Age < 40") \
             .groupby("Country") \
             .count()