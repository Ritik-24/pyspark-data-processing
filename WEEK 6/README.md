# Week 6 Assignment: Apache Spark Data Pipeline

## 1. Spark Architecture Overview
This project leverages Apache Spark’s distributed computing framework to process datasets efficiently.

* **Driver:** The central coordinator that runs the `main()` function, initializes the `SparkSession`, and converts the user’s code into a logical **DAG (Directed Acyclic Graph)**.
* **Cluster Manager:** Manages physical hardware resources (CPU/RAM) across the cluster nodes (e.g., YARN, Kubernetes, or Local Standalone).
* **Executors:** Distributed worker processes responsible for executing assigned tasks and storing data in memory or on disk.

### Execution Mode
This project is configured for **Local Mode**, utilizing local machine threads to act as both Driver and Executor for efficient development and testing.

## 2. Technical Design & Optimization
* **Lazy Evaluation:** Transformations are not executed immediately. Spark records them in a DAG and uses the **Catalyst Optimizer** to streamline the plan before an **Action** (e.g., `.show()`, `.write()`) is triggered.
* **Schema Handling:** Explicit `StructType` schema definition is enforced during ingestion to prevent the overhead of automatic schema inference, which requires a full scan of the raw data.
* **Storage Strategy:** Data is ingested from raw CSV files and persisted into **Parquet format**. Parquet is a columnar storage format that optimizes performance via:
    * **Predicate Pushdown:** Skipping unnecessary data blocks during read operations.
    * **Column Projection:** Reading only required columns, significantly reducing I/O latency.

## 3. Data Pipeline Workflow
1. **Extract:** Read raw CSV data with an enforced schema.
2. **Transform:** * Renamed columns for readability.
    * Casted data types (e.g., String to Timestamp).
    * Handled `NULL` values.
    * Added calculated business metrics.
3. **Load:** Saved the processed DataFrame into an optimized, partitioned Parquet folder.

## 4. Performance Best Practices
* **Avoid `collect()`:** Used `show()` for debugging to prevent potential OutOfMemory (OOM) errors by not pulling large datasets into the Driver's memory.
* **Parquet vs. CSV:** Transitioned from CSV to Parquet to leverage metadata-driven performance and storage compression.
