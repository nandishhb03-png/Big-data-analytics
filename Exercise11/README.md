# Exercise 11 - Apache Spark Word Count

## Objective
Install Apache Spark and perform Word Count using PySpark.

## Tools Used
- Ubuntu (WSL)
- Java 21
- Apache Spark 4.1.1
- PySpark

## Tasks Performed
- Installed Java
- Installed Apache Spark
- Configured SPARK_HOME
- Verified Spark installation
- Executed Word Count using parallelize()
- Executed Word Count using sample.txt

## Output

### Word Count using parallelize()

```
+------+-----+
| word |count|
+------+-----+
|Hello | 3   |
|Spark | 3   |
|world | 1   |
|for   | 1   |
|great | 1   |
|is    | 1   |
|data  | 1   |
|big   | 1   |
|and   | 1   |
|Python| 1   |
+------+-----+
```

### Word Count using sample.txt

```
+------+-----+
| word |count|
+------+-----+
|Spark | 3   |
|Hello | 2   |
|Fast  | 1   |
|Apache| 1   |
|is    | 1   |
|Python| 1   |
+------+-----+
```

## Result

Apache Spark was installed successfully and the Word Count program executed successfully using both in-memory data and a text file.
