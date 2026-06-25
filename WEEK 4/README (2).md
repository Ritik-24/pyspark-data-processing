# Azure Cloud Fundamentals and Data Pipeline Implementation using ADF

## 🎯 Objective
To understand core Microsoft Azure cloud concepts and architect a secure, metadata-validated, end-to-end automated data ingestion pipeline using an Azure Storage Account and Azure Data Factory (ADF).

---

## 🛠️ Assignment Tasks & Implementation

### Task 1: Explore Azure Portal & Resource Group Creation
* **Action:** Created a logical deployment container named `rg-azure-pipeline-demo` in the **South India** region to isolate all related cloud assets.
* **Deliverable:**
![Resource Group Overview](Resource_Group.png)

### Task 2: Storage Architecture Setup
* **Action:** Provisioned a general-purpose v2 cloud storage account (`storagedemopipelinerit`), created a blob container named `source-data`, and uploaded `Sample - Superstore.csv` (Size: 2.18 MiB, Hot access tier).
* **Deliverable:**
![Storage Container Overview](Storage_container.png)
![Storage Container with Uploaded File](Storage_container_csv.png)

### Task 3: Azure Data Factory (ADF) Foundations
* **Action:** Created the data integration platform instance (`adf-pipeline-demo-rit`) and established core structures:
  * **Linked Service:** `ls_BlobStorage` connecting ADF safely to the storage account via Account Keys.
  * **Datasets:** Defined `ds_SourceCSV` (pointing to the raw CSV) and `ds_DestinationCSV` (targeting the output path).
  * **Get Metadata Activity:** Added validation parameters using an `Exists` evaluation type to check file integrity before streaming data.
* **Deliverables:**
![Linked Service Properties](Linked_Service.png)
![Dataset Properties](Datasets.png)
![Get Metadata Activity Configuration](Metadata.png)

### Task 4: Ingestion Pipeline Development
* **Action:** Built a sequential processing workflow canvas named `pl_BlobToBlob_Demo`. Connected the `Get Metadata` activity validation check to a `Copy Data` activity via a green success constraint.
* **Deliverable:**
![Pipeline Design Canvas](Pipeline_design.png)

### Task 5: Pipeline Execution & Verification
* **Action:** Triggered a manual test execution run using the **Debug** engine. 
* **Metrics:** Total processing runtime took **36 seconds** (`Get Metadata1`: 16s | `Copy data1`: 20s) with a status of **Succeeded**.
* **Deliverables:**
![Pipeline Execution View](Pipeline_execution.png)

### Task 6: Identity and Access Management (IAM) Role Configuration
* **Action:** Secured access boundaries without exposing root passwords using Azure Role-Based Access Control (RBAC). Provided the ADF system identity explicit **Storage Blob Data Contributor** and **Storage Blob Data Reader** privileges over the storage account.
* **Deliverable:**
![Role Assignments Received](Role_Assignment.png)

---

## 🚀 Mini Project Final Conclusion Summary
The data engineering target objective has been fully achieved. The engineered architecture successfully orchestrates automated data migration:
1. **Pre-Validation:** The pipeline reads incoming block blobs and parses structural boundaries without triggering hard failure exits using Metadata verification.
2. **Replication & Execution:** Upon successful verification, the engine maps parameters row-by-row, dynamically creating a physical `output/` directory inside the blob namespace containing the perfectly preserved dataset file.
3. **Enterprise Security:** Infrastructure data streams remain identity-isolated using native platform RBAC assignments rather than public exposure tokens.
![Successful Debug Execution Run Logs](Output.png)

