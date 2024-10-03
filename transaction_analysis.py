import pandas as pd

def analyze_transactions(df):
    """Print out transaction analysis."""
    # Total transactions per bank
    transactions_per_bank = df['Transferror_Bank'].value_counts()
    print("Total Transactions per Bank:")
    print(transactions_per_bank)
    
    # Total amount transferred per bank
    amount_per_bank = df.groupby('Transferror_Bank')['Amount'].sum()
    print("\nTotal Amount Transferred per Bank:")
    print(amount_per_bank)
    
    # Most frequent recipients
    transactions_per_recipient = df['Transferror_Name'].value_counts()
    print("\nMost Frequent Recipients:")
    print(transactions_per_recipient)
    
    # Total amount transferred to each recipient
    amount_per_recipient = df.groupby('Transferror_Name')['Amount'].sum()
    print("\nTotal Amount Transferred to Each Recipient:")
    print(amount_per_recipient)
