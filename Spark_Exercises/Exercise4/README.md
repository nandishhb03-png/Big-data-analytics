# Spark Exercise 4 - ETL Pipeline

## Submitted By
Nandeesh H M

## Objective
Perform an ETL (Extract, Transform, Load) process using Apache Spark.

## Files
- employees.csv
- etl_pipeline.py
- output.txt

## ETL Steps

### Extract
Read employee data from a CSV file.

### Transform
- Remove rows with NULL values.
- Increase each employee's salary by 10%.

### Load
Save the transformed data into the `output_data` folder.

## Technologies Used
- Apache Spark 4.1.1
- PySpark
- Python
