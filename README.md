## Transaction Classification and Analysis
This project performs the extraction, categorization, and classification of financial transactions based on predefined regular expressions. Additionally, it analyzes transaction data and provides insights such as the total number of transactions, the total amount transferred, and the most frequent recipients, alongside visualizations. Machine learning techniques are also applied to predict transaction types.

**Workflow Overview**
**1. Loading the Dataset**
A CSV file containing transaction data is loaded into a pandas DataFrame 
        for analysis.
  **2. Regex-Based Data Extraction**
    Multiple regular expressions are used to extract important transaction details     like transferror name, transferror bank, and transaction ID from the narration     column in the dataset.The extracted details are stored in separate lists and       appended as new columns to the original DataFrame.
3. Data Categorization
The transactions are categorized into different types (such as UPI-P2A, ATM-CASH, POS, etc.) based on the narration patterns and the nature of the transaction.
Transactions are further categorized into broad categories (Food, Shopping, Entertainment, etc.) based on the transferror name.
4. Clustering and Standardization
The extracted and categorized data is prepared for clustering by applying One-Hot Encoding to the categorical variables.
StandardScaler is used to standardize the features before clustering.
5. Insights and Visualization
Total Transactions per Bank: The number of transactions associated with each bank is calculated and displayed.
Total Amount Transferred per Bank: The total amount of money transferred to each bank is calculated and displayed.
Most Frequent Recipients: The recipients with the highest number of transactions are displayed.
Total Amount Transferred per Recipient: The total amount transferred to each recipient is calculated.
These insights are visualized using Seaborn bar plots.
6. Machine Learning Model
A Random Forest Classifier is trained on the extracted and categorized transaction data.
The dataset is split into training and testing sets.
The model is used to predict transaction types, and the results are evaluated using accuracy and classification metrics.
The feature importance is displayed to understand which features have the most influence on the predictions.
7. Saving Results
The final DataFrame, including the extracted transaction details and the predicted transferror types, is saved to an Excel file (Grouped_Transferor_Banks.xlsx).
Requirements
Python 3.x
Libraries:
pandas
numpy
matplotlib
seaborn
scikit-learn
openpyxl
Install the required libraries using the following command:

Copy code
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
Input Data
The input data should be provided in a CSV file (transaction.csv) that contains at least the following columns:
Particulars: Descriptive narration of the transaction.
Credit: Amount credited in the transaction.
Debit: Amount debited in the transaction.
Output
Visualizations: Several bar plots for insights into transaction data.
Excel File: The final categorized and classified transaction data will be saved as an Excel file (Grouped_Transferor_Banks.xlsx).
How to Run
Place the transaction.csv file in the working directory.
Run the Python script to process the transactions and generate insights.
The results will be saved in the Grouped_Transferor_Banks.xlsx file in the specified directory.
Advanced Features
The code categorizes transaction narrations based on predefined regular expressions and generalizes the names of transferors.
A Random Forest Classifier is trained to predict the type of transaction based on the extracted features.
Feature importance is displayed to highlight which features contribute the most to the model’s predictions.
