
import pdfplumber
import pandas as pd

# Open the PDF file
pdf_path ='/Users/terminalorders/Desktop/Invoices SL/Invoice 007272 Paymentsave.pdf'
with pdfplumber.open(pdf_path) as pdf:
    all_data = []
    for page in pdf.pages:
        # Extract tables on each page
        tables = page.extract_tables()
        for table in tables:
            # Append table data
            all_data.extend(table)
# Convert the extracted data into a DataFrame
df = pd.DataFrame(all_data)

# Save to a CSV file
csv_path = 'output.csv'
df.to_csv(csv_path, index=False, header=False)

import csv

# File path to your CSV file
file_path = csv_path

# Rows to include in the sum (case-sensitive, match description exactly as in CSV)
rows_to_sum = [
    'Desk5000',
    'Desk3500',
    'Move3500 GPRS',
    'Move3500 BT/Wi-Fi',
    'Move5000',
'A920/A920 Pro Charging Base',
'A920 Pro',
'A920/A920 Pro Bluetooth Base',
'A35',
'A35 Wi-Fi',
'Saturn 1000 & Base',
'Repairs and Refurbs',
'Service Credit',
'A80',
'Repairs and Refurbs'
]

# Initialize the total sum
total_sum = 0.0

# Read the CSV file and process rows
with open(file_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        description, quantity, unit_price, total_price = row
        if description in rows_to_sum:
            print((total_price))
            total_sum += float(total_price.replace("(", "").replace(",", "").replace("£", "").replace(")", ""))  # Convert to float
            
# Print the total sum
print(f"The total sum of the selected rows is: £{total_sum:.2f}")

