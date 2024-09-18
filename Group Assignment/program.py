import pandas as pd
import os

# Define the paths
input_file = "combined.xlsx"
output_file = 'Combined_YesNoNumerical.xlsx'

# Load the Excel file
df = pd.read_excel(input_file)

print("Original DataFrame:")
print(df.head())

# Replace 'Yes' with 1 and 'No' with 0 in all columns
df = df.replace({'Yes': 1, 'No': 0})

# Save the modified DataFrame back to an Excel file
df.to_excel(output_file, index=False)

# Check if the file was created successfully
if os.path.exists(output_file):
    print(f"File '{output_file}' created successfully.")
else:
    print(f"Failed to create the file '{output_file}'.")

print("Modified DataFrame:")
print(df.head())