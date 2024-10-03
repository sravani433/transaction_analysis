import pandas as pd

def export_to_excel(df, output_path):
    """Save the dataframe to an Excel file."""
    df.to_excel(output_path, sheet_name='Grouped_Transferr', index=False)
    print(f"Data exported to {output_path}")
