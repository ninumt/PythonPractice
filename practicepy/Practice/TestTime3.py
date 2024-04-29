import re
from datetime import datetime

# Function to extract dates in ISO 8601 format from a string
def extract_iso_dates(text):
    iso_date_pattern = r'\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}\b'
    return re.findall(iso_date_pattern, text)

# Function to parse and filter unique ISO 8601 format dates
def filter_unique_iso_dates(dates):
    unique_dates = set()
    filtered_dates = []
    for date_str in dates:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
            if date_obj not in unique_dates:
                unique_dates.add(date_obj)
                filtered_dates.append(date_obj)
        except ValueError:
            pass  # Skip if the date format is invalid
    return filtered_dates

# Read dates from input file
input_file_path = '../IOFiles/input.txt'
output_file_path = '../IOFiles/output.txt'

with open(input_file_path, 'r') as file:
    text = file.read()

# Extract dates in ISO 8601 format
iso_dates = extract_iso_dates(text)

# Filter unique ISO 8601 format dates
unique_dates = filter_unique_iso_dates(iso_dates)

# Write filtered dates to output file
with open(output_file_path, 'w') as file:
    for date_obj in unique_dates:
        file.write(date_obj.strftime('%Y-%m-%dT%H:%M:%S%z') + '\n')
