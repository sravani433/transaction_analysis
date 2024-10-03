import pandas as pd

# Load the Excel file
excel_file = 'C:\\Users\\admin\\Downloads\\transaction 1.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file)

# Convert to CSV
csv_file = 'transaction.csv'  # Specify the output CSV file path
df.to_csv(csv_file, index=False)

print(f"Excel file '{excel_file}' has been converted to '{csv_file}'.")
