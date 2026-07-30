from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import sum, col

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

sales_data = [
    Row(date="2024-01-01", product="Laptop", price=1000, quantity=2, city="Delhi"),
    Row(date="2024-01-01", product="Mouse", price=50, quantity=5, city="Mumbai"),
    Row(date="2024-01-02", product="Laptop", price=1000, quantity=1, city="Bangalore"),
]

df = spark.createDataFrame(sales_data)

print("Original Data")
df.show()

print("Revenue by Product")
df_grouped = df.groupBy("product").agg(
    sum("price").alias("total_revenue"),
    sum("quantity").alias("total_quantity")
)

df_grouped.show()

print("Revenue by City")
df.groupBy("city").agg(
    sum("price").alias("revenue")
).orderBy(col("revenue").desc()).show()

spark.stop()
