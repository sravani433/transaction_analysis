# Transaction Categorization and Clustering Analysis

This project performs transaction categorization, analysis, and clustering on financial transaction data from a CSV file. It includes various stages such as extracting relevant information using regular expressions, categorizing transactions based on predefined categories, and applying machine learning models to predict transfer types and provide insights into transaction data.

## Features

- **Transaction Categorization**: Extracts details such as transferror name, ID, bank, category, and type from transaction narrations using regex patterns.
- **Data Cleaning**: Handles missing values and formats data for further analysis.
- **Clustering and Grouping**: Groups transactions by transferor names and banks to gain insights into transaction distribution and frequency.
- **Machine Learning**: Uses Random Forest Classifier to predict the transferror type based on transaction details.
- **Visualization**: Generates bar plots to visualize total transactions and amounts per bank and recipients.
- **Export to Excel**: Saves the processed and grouped transaction data into an Excel file.

## Steps for Execution

1. **CSV File Loading**: 
   The script starts by loading a CSV file containing transaction data (`transaction.csv`).

2. **Data Extraction**:
   - Transaction narration details such as ID, name, bank, type, and category are extracted using predefined regex patterns.
   - Several transaction types are handled, such as `ATM-CASH`, `POS`, `UPI`, `IMPS`, `ECOM`, and more.

3. **Transaction Categorization**:
   - Transactions are categorized into different sections like `Food`, `Entertainment`, `Shopping`, etc., based on the transferor name.
   - These categories are used to enrich the data and gain deeper insights into spending habits.

4. **Data Transformation**:
   - The dataset is transformed to prepare it for machine learning, including handling missing values and converting categorical data into numeric form using one-hot encoding.
   
5. **Clustering & Grouping**:
   - The data is grouped by `Transferror Name` and `Transferror Bank` to show the distribution of transactions across banks and individuals.
   - Clustering algorithms such as KMeans can also be applied to identify patterns in the data.

6. **Visualization**:
   - Various bar plots are generated to provide insights:
     - Total transactions per bank.
     - Total amount transferred per bank.
     - Most frequent recipients of transactions.
     - Total amount transferred to each recipient.
     
7. **Machine Learning**:
   - The model uses a Random Forest Classifier to predict the `Transferror Type` based on transaction features.
   - After training, the model evaluates its performance using accuracy scores and classification reports.

8. **Feature Importance**:
   - The script outputs feature importance to understand which factors have the highest impact on predicting the `Transferror Type`.

9. **Export Results**:
   - The processed and analyzed data is saved to an Excel file (`Grouped_Transferor_Banks.xlsx`), which includes the newly predicted `Transferror Type`.

## Requirements

- Python 3.x
- Required Libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `openpyxl`
  - `matplotlib`
  - `seaborn`

 # Running the Files

Follow the steps below to execute the scripts in the correct order:

## 1. Place the `transaction.csv` file

Ensure the `transaction.csv` file containing the transaction data is in the same directory as the scripts.

## 2. Run `main.py`

The primary script to process the transaction data and perform analysis. This script will:

- Load the CSV file.
- Categorize transactions.
- Apply machine learning to predict transferror types.
- Generate visualizations for transactions and amounts.
- Save the results to an Excel file (`Grouped_Transferor_Banks.xlsx`).

   To run the script:
     ```bash
    python main.py

 ## Output Files
 
   Excel File: The final grouped and categorized transactions will be saved to 
   Grouped_Transferor_Banks.xlsx.
   
 ## Visualizations
 - Bar plots for total transactions and amounts are generated for:
 - Transactions per bank.
 - Amount transferred per bank.
 - Most frequent recipients.
 - Total amount transferred to each recipient.
