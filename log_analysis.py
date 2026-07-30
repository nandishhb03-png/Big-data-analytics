
from pyspark.sql import SparkSession
import re

spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()
sc = spark.sparkContext

logs = sc.textFile("/home/nandi/Big-data-analytics/Spark_Exercises/Exercise3/logs.txt")

def parse_log(line):
    ip = re.search(r'^(\d+\.\d+\.\d+\.\d+)', line).group(1)
    status = re.search(r' (\d{3})$', line).group(1)
    return (ip, status)

parsed = logs.map(parse_log)

print("=" * 50)
print("Spark Exercise 3 - Log Analysis")
print("Submitted By: Nandeesh H M")
print("=" * 50)

print("\nIP Address Count")
ip_counts = parsed.map(lambda x: (x[0], 1)).reduceByKey(lambda a, b: a + b)

for ip, count in ip_counts.collect():
    print(f"{ip}: {count}")

print("\nStatus Code Count")
status_counts = parsed.map(lambda x: (x[1], 1)).reduceByKey(lambda a, b: a + b)

for status, count in status_counts.collect():
    print(f"Status {status}: {count}")

spark.stop()
