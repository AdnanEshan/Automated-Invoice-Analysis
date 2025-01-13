
import pdfplumber
import pandas as pd

# Open the PDF file
#Invoice 007272 Paymentsave.pdf March
#Invoice 008110 Paymentsave.pdf Oct
#Invoice 007505 Paymentsave.pdf May
#Invoice 006932 Paymentsave.pdf Dec
#Invoice 007158 Paymentsave.pdf Feb
#Invoice 007388 Paymentsave.pdf April
#Invoice 007042 Paymentsave.pdf Jan
pdf_path ='/Users/terminalorders/Desktop/Invoices SL/Invoice 006932 Paymentsave.pdf'
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
    "TMS, Software & 2nd Line Charges",
"PAX Software and PAX Store Licence",
"PAX WEB Link",
"PAX Goinsights",
"Elavon Remote Key Load (PAX)",
#"SwapIT Charges",
"Technical Helpdesk",
#"Additional Courier Charges",
"Testing/Restocking Fee",
"Collections"
#bad "Returned to Sender/Re-despatches"
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
            print(total_price)
            total_sum += float(total_price.replace(",", "").replace("£", ""))  # Convert to float
            
# Print the total sum
print(f"The total sum of the selected rows is: £{total_sum:.2f}")

