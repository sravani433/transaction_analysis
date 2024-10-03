import matplotlib.pyplot as plt
import seaborn as sns

def plot_transactions_per_bank(df):
    """Plot total transactions per bank."""
    transactions_per_bank = df['Transferror_Bank'].value_counts()
    plt.figure(figsize=(15, 10))
    sns.barplot(x=transactions_per_bank.index, y=transactions_per_bank.values, palette='viridis')
    plt.title('Total Transactions per Bank')
    plt.xlabel('Bank')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_amount_transferred_per_bank(df):
    """Plot total amount transferred per bank."""
    amount_per_bank = df.groupby('Transferror_Bank')['Amount'].sum()
    plt.figure(figsize=(15, 10))
    sns.barplot(x=amount_per_bank.index, y=amount_per_bank.values, palette='viridis')
    plt.title('Total Amount Transferred per Bank')
    plt.xlabel('Bank')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_frequent_recipients(df):
    """Plot most frequent recipients."""
    transactions_per_recipient = df['Transferror_Name'].value_counts()
    plt.figure(figsize=(70, 12))
    sns.barplot(x=transactions_per_recipient.index, y=transactions_per_recipient.values, palette='viridis')
    plt.title('Most Frequent Recipients')
    plt.xlabel('Recipient')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_amount_per_recipient(df):
    """Plot total amount transferred to each recipient."""
    amount_per_recipient = df.groupby('Transferror_Name')['Amount'].sum()
    plt.figure(figsize=(70, 12))
    sns.barplot(x=amount_per_recipient.index, y=amount_per_recipient.values, palette='viridis')
    plt.title('Total Amount Transferred to Each Recipient')
    plt.xlabel('Recipient')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
