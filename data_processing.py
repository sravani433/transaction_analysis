import pandas as pd
import re

# Function to load the CSV file
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to extract transaction details using regex patterns
def extract_transaction_details(df):
    # Regex patterns
    patterns = {
        'ATM-CASH': r'ATM-CASH/([A-Za-z0-9\s\/\,]+)/([A-Za-z]+)+/(\d{6})',
        'POS': r'POS/([A-Za-z\s]+)/([A-Za-z]+)/(\d{6})/',
        'UPI-P2A': r'UPI/P2A/(\d+)/([A-Za-z\s_]+)/([A-Za-z\s_]+)/',
        'UPI-P2M': r'UPI/P2M/(\d+)/([A-Za-z\s_]+)/([A-Za-z\s_]+)/',
        'UPI-CR': r'UPI/CRADJ/(\d+)/',
        'IMPS': r'IMPS/[A-Z0-9]+/(\d+)/([A-Za-z0-9]+)/([A-Za-z0-9]+)/',
        'ECOM': r'ECOM\sPUR/([A-Za-z0-9*\s]+)/([a-zA-Z0-9]+)/\d{6}/',
        'NBSM': r'NBSM/(\d+)/([A-Za-z0-9\s()]+)',
        'INB-IFT' : r'INB/IFT/([A-Za-z0-9\s]+)/([A-Za-z0-9\s]+)',
        'MOB-TPFT': r'MOB/TPFT/([A-Za-z0-9\s]+)/([A-Za-z0-9\s\d]+)',
        'ACH-CR': r'ACH-CR-([A-Za-z\s\(\(\.]+)-NACH-\s*((\d+)(?:\s*-\s*(\d+))?)',
        'NEFT': r'NEFT/([A-Za-z0-9\s]+)/([A-Za-z0-9\s]+)/([a-zA-Z0-9\s]+)/',
        'INB-BULK': r'INB-BULK- UPLD/([a-zA-Z0-9\s]+)/([a-zA-Z0-9]+)/([a-zA-Z]+)/([a-zA-Z0-9]+)/([a-zA-Z0-9]+)',  
        'Locker': r'Locker Rent Recovery For([A-Za-z0-9\s-]+)',
        'CASH-WDL': r'SAK/CASH WDL/([a-zA-Z0-9\s]+)/\d+/([a-zA-Z0-9]+)/([a-zA-Z0-9]+)',
        'CARD':r'BRN-PYMT-CARD-(\d+)',
        'labs':r'([a-zA-Z0-9\s-]+)/',
        'int':r'(\d+):(a-zA-Z0-9)'
    }

    # Lists to store extracted values
    transferror_id_list = []
    transferror_name_list = []
    transferror_bank_list = []
    category_list = []
    transferror_type_list = []

    # Extract details based on patterns
    for index, row in df.iterrows():
        narration = row['Particulars']  # Column with transaction narrations
        matched = False
        for transaction_type, pattern in patterns.items():
            match = re.search(pattern, narration)
            if match:
                matched = True
                transaction_id, transferror_name, transferror_bank, category, transferror_type = extract_details_based_on_pattern(match, transaction_type)
                transferror_id_list.append(transaction_id)
                transferror_name_list.append(transferror_name)
                transferror_bank_list.append(transferror_bank)
                transferror_type_list.append(transferror_type)
                category_list.append(category)
                break
        if not matched:
            transferror_id_list.append("Unknown")
            transferror_name_list.append("Unknown")
            transferror_bank_list.append("Unknown")
            transferror_type_list.append("Unknown")
            category_list.append("Unknown")

    # Add new columns to the dataframe
    df['Transferror_ID'] = transferror_id_list
    df['Transferror_Name'] = transferror_name_list
    df['Transferror_Bank'] = transferror_bank_list
    df['Category'] = category_list
    df['Transferror_Type'] = transferror_type_list
    df['Amount'] = df['Credit'].fillna(0) - df['Debit'].fillna(0)

    return df

# Helper function to extract details based on regex match
def extract_details_based_on_pattern(match, transaction_type):
    if transaction_type == 'ATM-CASH':
        return match.group(2), match.group(1), "Unknown", "Unknown", "ATM-CASH"
    elif transaction_type == 'POS':
        return match.group(2), match.group(1), "Unknown", "POS", "POS"
    elif transaction_type == 'UPI-P2A':
        return match.group(1), match.group(2), match.group(3), "Unknown", "By UPI-Person 2 Account"
    elif transaction_type == 'UPI-P2M':
        return match.group(1), match.group(2), match.group(3), "Unknown", "By UPI-Person 2 Merchant"
    elif transaction_type == 'IMPS':
        return match.group(1), match.group(2), match.group(3), "Unknown", "IMPS"
    elif transaction_type == 'ECOM':
        return match.group(2), match.group(1), "Unknown", "Unknown", "ECOM"
    elif transaction_type == 'NBSM':
        return match.group(1), match.group(2), "Unknown", "Unknown", "NBSM"
    elif transaction_type == 'INB-IFT':
        return "Unknown", match.group(1), "Unknown", match.group(2), "INB-IFT"
    elif transaction_type == 'MOB-TPFT':
        return match.group(2), match.group(1), "Unknown", "Unknown", "MOB-TPFT"
    elif transaction_type == 'ACH-CR':
        return match.group(2), match.group(1), "Unknown", "Unknown", "ARH-CR"
    elif transaction_type == 'NEFT':
        return match.group(1), match.group(2), match.group(3), "Unknown", "NEFT"
    elif transaction_type == 'INB-BULK':
        return match.group(1), match.group(5), "Unknown", match.group(2), "INB-BULK"
    elif transaction_type == 'CASH-WDL':
        return match.group(1), match.group(2), "Unknown", match.group(3), "Cash withdrawal"
    elif transaction_type == 'Locker':
        return "Unknown", "Unknown", "Unknown", match.group(1), "Locker rent recovery"
    elif transaction_type == 'labs':
        return "Unknown", match.group(1), "Unknown", "Unknown", "Transfer"
    elif transaction_type == 'CARD':
        return match.group(1), "Unknown", "Unknown", "Unknown", "Payment through card"
    elif transaction_type == 'int':
        return match.group(1), "Unknown", "Unknown", "Unknown", "Int.Pd."
    elif transaction_type == 'UPI-CR':
        return match.group(1), "Unknown", "Unknown", "Unknown", "UPI-CRADJ"
    return "Unknown", "Unknown", "Unknown", "Unknown", "Unknown"

# Function to categorize transactions based on transferor name
def categorize_transaction(transferor_name, categories):
    transferor_name = transferor_name.lower()  # Convert transferor name to lowercase
    for category, sub_categories in categories.items():
        for sub_category, names in sub_categories.items():
            if any(name in transferor_name for name in names):
                return f"{category}-{sub_category if sub_category else 'General'}"
    return 'Unknown'

# Function to apply the categorization
def apply_categorization(df, categories):
    df['Transferror_Name'] = df['Transferror_Name'].str.lower()  # Convert all transferor names to lowercase
    df['Category'] = df['Transferror_Name'].apply(lambda name: categorize_transaction(name, categories))
    return df

# Function to save processed dataframe to Excel
def save_to_excel(df, output_path):
    df.to_excel(output_path, sheet_name='Processed_Transactions', index=False)
    print(f"Data saved to {output_path}")

