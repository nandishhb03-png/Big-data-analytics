from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()
sc = spark.sparkContext

text_file = sc.textFile("/home/nandi/sample.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)

for word, count in counts.collect():
    print(f"{word}: {count}")

spark.stop()
