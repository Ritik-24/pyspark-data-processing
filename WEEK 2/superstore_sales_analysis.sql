--STEP 2: EXPLORE THE TABLE STRUCTURE AND SAMPLE DATA
SELECT 
    COLUMN_NAME AS [Column Name], 
    DATA_TYPE AS [Data Type], 
    CHARACTER_MAXIMUM_LENGTH AS [Max Length],
    IS_NULLABLE AS [Allows Nulls]
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Sample - Superstore';

SELECT TOP (5) *
  FROM [Sample - Superstore]

-- STEP 3: Apply WHERE filters
SELECT 
    [Row_ID], 
    [Order_ID], 
    [Order_Date], 
    [Region], 
    [Category], 
    [Sales]
FROM [Sample - Superstore]
WHERE [Region] = 'South'              
  AND [Category] = 'Technology'       
  AND [Order_Date] >= '2016-01-01'    
  -- Explicitly cast Sales text to decimal so it can safely compare to 100
  AND CAST([Sales] AS DECIMAL(18,4)) > 100;

  -- STEP 4: Apply GROUP BY for aggregations (sales, quantity, averages)
SELECT 
    [Region], 
    [Category], 
    ROUND(SUM(CAST([Sales] AS DECIMAL(18,2))), 2) AS [Total_Sales],     -- Converts text to Decimal for SUM
    SUM(CAST([Quantity] AS INT)) AS [Total_Quantity],                    -- Converts text to Integer for SUM
    ROUND(AVG(CAST([Profit] AS DECIMAL(18,2))), 2) AS [Avg_Profit]       -- Converts text to Decimal for AVG
FROM [Sample - Superstore]
GROUP BY [Region], [Category]
ORDER BY [Region] ASC, [Total_Sales] DESC;

-- STEP 5: SORT AND LIMIT RESULTS
SELECT TOP 5 
    [Product_Name], 
    ROUND(SUM(CAST([Sales] AS DECIMAL(18,4))), 2) AS [Total_Sales]
FROM [Sample - Superstore]
GROUP BY [Product_Name]
ORDER BY [Total_Sales] DESC;

SELECT TOP 5 
    [Category], 
    [Sub_Category], 
    ROUND(SUM(CAST([Profit] AS DECIMAL(18,4))), 2) AS [Total_Profit]
FROM [Sample - Superstore]
GROUP BY [Category], [Sub_Category]
ORDER BY [Total_Profit] DESC;

-- STEP 6: SOLVE BUSINESS USE CASES (CORRECTED WITH UNDERSCORES)
-- Case A: Monthly Sales Trends 
SELECT 
    YEAR(CAST([Order_Date] AS DATE)) AS [Order_Year], 
    MONTH(CAST([Order_Date] AS DATE)) AS [Order_Month], 
    ROUND(SUM(CAST([Sales] AS DECIMAL(18,4))), 2) AS [Monthly_Sales]
FROM [Sample - Superstore]
GROUP BY YEAR(CAST([Order_Date] AS DATE)), MONTH(CAST([Order_Date] AS DATE))
ORDER BY [Order_Year] ASC, [Order_Month] ASC;

-- Case B: Top 5 Highest-Spending Customers 
SELECT TOP 5 
    [Customer_ID], 
    [Customer_Name], 
    ROUND(SUM(CAST([Sales] AS DECIMAL(18,4))), 2) AS [Total_Sales]
FROM [Sample - Superstore]
GROUP BY [Customer_ID], [Customer_Name]
ORDER BY [Total_Sales] DESC;

-- Case C: Duplicate Verification 
SELECT [Row_ID], COUNT(*) AS [Occurrence_Count]
FROM [Sample - Superstore]
GROUP BY [Row_ID]
HAVING COUNT(*) > 1;
GO

-- STEP 7: VALIDATE RESULTS (ROW COUNTS & DATA QUALITY AUDIT)
SELECT 
    COUNT(*) AS [Total_Rows],
    SUM(CASE WHEN [Order_ID] IS NULL OR [Order_ID] = '' THEN 1 ELSE 0 END) AS [Null_Or_Empty_Orders],
    SUM(CASE WHEN [Sales] IS NULL OR [Sales] = '' THEN 1 ELSE 0 END) AS [Null_Or_Empty_Sales]
FROM [Sample - Superstore];
GO