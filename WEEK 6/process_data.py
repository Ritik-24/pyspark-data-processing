# Objective:
# Read -> Transform -> Filter -> Write

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col
import traceback

# STEP 1 : Create Spark Session
spark = (
    SparkSession.builder
    .appName("Week6_Pipeline")
    .master("local[*]")
    .config(
        "spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version",
        "2"
    )
    .config("spark.sql.sources.commitProtocolClass",
            "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")
    .config("spark.hadoop.fs.file.impl",
            "org.apache.hadoop.fs.LocalFileSystem")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("Spark Session Created Successfully")


# STEP 2 : Define Explicit Schema
schema = StructType([
    StructField("InvoiceNo", StringType(), True),
    StructField("StockCode", StringType(), True),
    StructField("Description", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("InvoiceDate", StringType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("CustomerID", IntegerType(), True),
    StructField("Country", StringType(), True)
])

# STEP 3 : Read CSV File
print("\n READING CSV ")

csv_df = spark.read \
    .option("header", "true") \
    .schema(schema) \
    .csv("data.csv")

print("CSV Loaded Successfully.")

csv_df.printSchema()

csv_df.show(5, truncate=False)

print("CSV Record Count :", csv_df.count())

# STEP 4 : Read Parquet File
print("\n READING PARQUET ")

try:

    parquet_df = spark.read.parquet("data.parquet")

    print("Parquet Loaded Successfully.")

    parquet_df.printSchema()

    parquet_df.show(5, truncate=False)

    print("Parquet Record Count :", parquet_df.count())

except Exception:

    print("Unable to read Parquet File.\n")
    traceback.print_exc()

# STEP 5 : Handle Null Values
print("\n HANDLING NULL VALUES ")

df = csv_df.fillna({
    "Description": "Unknown Product",
    "CustomerID": 0
})

# STEP 6 : Rename Column
print("\n RENAMING COLUMN ")

df = df.withColumnRenamed(
    "Description",
    "ProductDescription"
)

# STEP 7 : Cast Data Types

print("\n CASTING DATA TYPES ")

df = df.withColumn("Quantity", col("Quantity").cast("int"))

df = df.withColumn("UnitPrice", col("UnitPrice").cast("double"))

# STEP 8 : Add New Column
print("\n ADDING NEW COLUMN ")

df = df.withColumn(
    "TotalAmount",
    col("Quantity") * col("UnitPrice")
)

# STEP 9 : Filter Records
print("\n FILTERING DATA ")

filtered_df = df.filter(
    (col("Quantity") > 0) &
    (col("UnitPrice") > 0)
)

# STEP 10 : Select Required Columns
print("\n SELECTING REQUIRED COLUMNS ")

final_df = filtered_df.select(
    "InvoiceNo",
    "StockCode",
    "ProductDescription",
    "Quantity",
    "UnitPrice",
    "TotalAmount",
    "Country"
)

# STEP 11 : Display Processed Data
print("\n PROCESSED DATA ")

final_df.show(10, truncate=False)

print("Processed Record Count :", final_df.count())

# STEP 12 : Write Processed CSV
print("\n WRITING CSV ")

try:

    (final_df
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv(r"D:\CELEBAL\WEEK 6\processed_csv"))

    print("Processed CSV Saved Successfully.")

except Exception:

    print("\nCSV Writing Failed.\n")
    traceback.print_exc()

# STEP 13 : Write Processed Parquet
print("\n WRITING PARQUET n")

try:

    (final_df
 .coalesce(1)
 .write
 .mode("overwrite")
 .parquet(r"D:\CELEBAL\WEEK 6\processed_parquet"))

    print("Processed Parquet Saved Successfully.")

except Exception:

    print("\nParquet Writing Failed.\n")
    traceback.print_exc()

# STEP 14 : Performance Insights
print("\n PERFORMANCE INSIGHTS ")

print("1. Spark uses Lazy Evaluation.")
print("2. Transformations execute only when an Action is called.")
print("3. show() and count() are Actions.")
print("4. filter(), select(), withColumn() are Transformations.")
print("5. Parquet is faster than CSV because it is columnar.")
print("6. Spark creates a DAG before execution.")
print("7. Predicate Pushdown improves Parquet performance.")
print("8. Avoid collect() on large datasets.")

# STEP 15 : Stop Spark
spark.stop()
print("Spark Session Stopped Successfully.")
print("Program Executed Successfully.")