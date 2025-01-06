import pandas as pd
import os

# Input file path
excel_file = "filepath.xlsx"

# Output directory for CSV files
output_dir = "output_csv_files"
os.makedirs(output_dir, exist_ok=True)  

# Load the Excel file
excel_data = pd.ExcelFile(excel_file)

# Iterate through each sheet and save as CSV
for sheet_name in excel_data.sheet_names:
    # Read the sheet into a DataFrame
    df = excel_data.parse(sheet_name)
    
    # Create a CSV file name based on the sheet name
    csv_file = os.path.join(output_dir, f"{sheet_name}.csv")
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Saved sheet '{sheet_name}' to '{csv_file}'")

print("Done")
