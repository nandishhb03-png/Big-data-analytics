# Exercise 5: Hadoop Streaming with Python (MapReduce)

## Aim
To perform Hadoop MapReduce using Python Streaming for analyzing sales data and calculating the total sales for each city.

---

## Objective
- Generate a sample sales dataset using Python.
- Create a Mapper program to process the sales records.
- Create a Reducer program to calculate the total sales for each city.
- Execute the MapReduce job using Hadoop Streaming.
- Store and view the output in HDFS.

---

## Requirements
- Ubuntu (WSL)
- Hadoop 3.5.0
- Python 3
- Java
- HDFS

---

## Files
- `generate_sales.py` – Generates sample sales data.
- `sales_data.csv` – Generated sales dataset.
- `mapper_city_sales.py` – Mapper program.
- `reducer_city_sales.py` – Reducer program.

---

## Procedure
1. Generate the sales dataset using Python.
2. Create Mapper and Reducer scripts.
3. Upload the dataset to HDFS.
4. Run the Hadoop Streaming MapReduce job.
5. Store the output in HDFS.
6. Display the final results.

---

## Expected Output
The program displays the total sales amount for each city after processing the sales dataset using Hadoop MapReduce.

Example:

```text
Ahmedabad   46874532.56
Bangalore   47281934.18
Chennai     46123456.22
Delhi       46987654.90
Mumbai      47456789.34
```

---

## Learning Outcome
- Learned Hadoop Streaming with Python.
- Understood the working of Mapper and Reducer.
- Learned how to upload files into HDFS.
- Executed a Hadoop MapReduce job successfully.
- Analyzed sales data using distributed processing.

---

## Conclusion
This experiment successfully demonstrated Hadoop Streaming using Python. The Mapper processed the sales records, the Reducer calculated the total sales for each city, and the output was generated successfully using Hadoop MapReduce.
