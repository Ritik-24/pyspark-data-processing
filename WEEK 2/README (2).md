## 📂 Project Structure

*   **`superstore_sales_analysis.sql`**: Comprehensive query script for data conditioning, aggregations, and business trend analysis on a flat enterprise dataset (Task 1).
*   **`shopease_ecommerce_analysis.sql`**: Production-ready relational schema script containing DDL table definitions, data constraints, complex relational JOINs, conditional pivots, and safe ACID transactions (Task 2).

---

## 🛠️ Tech Stack & Database Environments
*   **Database Engine:** Microsoft SQL Server Express (v17.0.1000)
*   **IDE Interface:** SQL Server Management Studio (SSMS)
*   **Language Dialect:** Transact-SQL (T-SQL)

---

## 📈 Task 1: Global Superstore Sales Analytics

### 📌 Overview
This task involved performing granular deep-dive analysis on a high-volume retail transactions dataset. Due to flat-file text-import formatting quirks (where metrics like `Sales`, `Quantity`, and `Profit` were initially loaded as text fields with embedded decimal string values), a strategic **double-casting safeguard layer** was implemented across all queries to prevent conversion runtime errors.

### 🔍 Key Operational Discoveries & Metrics
*   **Data Quality Validation Layer:** Confirmed a flawless structural data footprint matching exactly **9,994 transaction records** with **0 missing entries or Null fields** across critical business indicators (`Order_ID`, `Sales`).
*   **Advanced Demographics Filter (Step 3):** Isolated exactly **45 high-yield rows** indicating premium consumer interactions specifically located in the *South* region purchasing *Technology* items exceeding $100 after 2016.
*   **Regional Product Portfolio Performance (Step 4):** Identified a major business operational risk in the **Central Region's Furniture** category, which generated a negative margin averaging **-$5.97** per transaction. Conversely, **Technology** products led all profiles, hitting per-sale profit averages between **$68 and $88**.
*   **Inventory Revenue Outliers (Step 5):** The single largest corporate revenue generator was identified as the **Canon imageCLASS 2200 Advanced Copier**, driving an extraordinary **$61,599.82** in gross sales volume.
*   **Seasonality & VIP Engagement (Step 6):** Trend groupings by calendar periods revealed massive, recurring revenue spikes concentrated in **September** and **December** (holiday shopping logistics cycles). The store's top high-net-worth client was identified as **Sean Miller**, tracking a lifetime brand spend of **$25,043.05**.

---

## 🛒 Task 2: ShopEase E-Commerce Relational Database System

### 📌 Overview
This task required designing, constructing, and optimizing a complete relational e-commerce database engine from the ground up for *ShopEase* (operating across electronics, clothing, and home categories in India). The database is architected with a strict 4-table transactional hierarchy: `customers` $\rightarrow$ `orders` $\rightarrow$ `order_items` $\leftarrow$ `products`.

### 🗄️ Relational Schema Engineering
*   **Primary Keys (`PK`):** Assigned unique identifiers to ensure row entity uniqueness (`customer_id`, `product_id`, `order_id`, `item_id`).
*   **Foreign Keys (`FK`):** Mapped strict relational integrity lines. Attempts to insert orders utilizing nonexistent parent records (e.g., `customer_id = 999`) are hard-blocked by database engine referential rules.
*   **Performance Optimization (Indexes):** Built specific indices (`idx_customers_city`, `idx_products_category`, `idx_orders_date`) to shift query lookups from costly linear table scans into log-time logarithmic searches.
*   **SARGable Query Rewriting:** Optimized performance by avoiding functions on columns in WHERE clauses (rewriting `YEAR(join_date) = 2024` into index-friendly literal boundary lookups).

### 📊 Query Result Metrics Matrix (Section C & E Results)

| Question | Assessed Business Insight | Generated Database Output |
| :--- | :--- | :--- |
| **Q13** | Total Orders Captured | **10** distinct transactions |
| **Q14** | Total Successful Revenue | **₹17,191.00** generated from 'Delivered' orders |
| **Q15** | Average Category Pricing | Clothing: **₹2,699.00** \| Electronics: **₹2,224.00** \| Home: **₹949.00** |
| **Q17** | Pricing Extremes (Max/Min) | Clothing: **₹4,599 / ₹799** \| Electronics: **₹3,499 / ₹899** |
| **Q18** | High-Value Category Sifting | **Clothing** and **Electronics** (Avg price exceeding ₹2,000) |
| **Q25** | Single-Row Operational Pivot | **Delivered Count: 6** \| **Not Delivered Count: 4** |

### 🛡️ Advanced Data Integrity & Financial Controls
*   **Domain Value Check Constraints:** Implemented defensive rules (`CHECK (unit_price > 0)`) that instantly reject erroneous financial inputs (e.g., rejecting an accidental insert of `-50.00`).
*   **ACID Compliance Implementation (Q27):** Built a critical, production-grade **Atomic Safe Transaction Block** utilizing explicit `BEGIN TRANSACTION`, `BEGIN TRY`, and `BEGIN CATCH` architecture. This design guarantees that if an inventory update or order item entry encounters a sudden hardware or database fault, the script triggers an immediate, absolute `ROLLBACK` to protect accounting lines from desynchronization.
