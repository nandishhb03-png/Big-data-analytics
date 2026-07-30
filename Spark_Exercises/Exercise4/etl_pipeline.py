from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder.appName("ETL_Pipeline").getOrCreate()

# Read CSV file
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

print("=" * 50)
print("Spark Exercise 4 - ETL Pipeline")
print("Submitted By: Nandeesh H M")
print("=" * 50)

print("\nOriginal Data")
df.show()

# Remove rows having NULL values
clean_df = df.dropna()

print("\nCleaned Data")
clean_df.show()

# Transformation: Increase salary by 10%
transformed_df = clean_df.withColumn(
    "Updated_Salary",
    col("Salary") * 1.10
)

print("\nTransformed Data")
transformed_df.show()

# Save transformed data
transformed_df.write.mode("overwrite").csv("output_data", header=True)

print("\nProcessed data saved successfully in 'output_data' folder.")

spark.stop()
