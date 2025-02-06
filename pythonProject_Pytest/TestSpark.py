from pyspark.sql import SparkSession
from pyspark.sql import functions as f

from lib.logger import Log4j
from lib.utils import get_spark_conf, load_source_read_df, count_by_country_df

if __name__ == "__main__":
    conf = get_spark_conf()

#we are not hardcoding app_name & master in here, but its in config
spark= SparkSession.builder \
    .config(conf = conf) \
    .getOrCreate()

logger = Log4j(spark)

#if we want to hardcode it then no need to move via conf and we can do as below
# spark= SparkSession.builder \
#     .appName("TestSpark") \
#     .master("local[3]") \
#     .getOrCreate()

logger.info("Starting loading of file")

survey_raw_df = load_source_read_df(spark)
filter_df = count_by_country_df(survey_raw_df)

survey_raw_df.show(5)
filter_df.show(5)

logger.info("End of Program")







