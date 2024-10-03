import data_processing
import transaction_analysis
import model_training
import visualizations
import export_data

def main():
    # Load and preprocess data
    df = data_processing.load_data('transaction.csv')
    
    # Extract transaction details using regex
    df = data_processing.extract_transaction_details(df)
    
    # Categorize transactions
    df = data_processing.categorize_transactions(df)
    
    # Analyze transactions (total transactions per bank, etc.)
    transaction_analysis.analyze_transactions(df)
    
    # Visualize the analysis results
    visualizations.plot_transactions_per_bank(df)
    visualizations.plot_amount_transferred_per_bank(df)
    visualizations.plot_frequent_recipients(df)
    visualizations.plot_amount_per_recipient(df)
    
    # Train RandomForest model and evaluate
    model = model_training.train_model(df)
    
    # Export results to Excel
    export_data.export_to_excel(df,'D:\\expense\\Grouped_Transferor_Banks.xlsx')
    
    print("Results saved.")

if __name__ == "__main__":
    main()
