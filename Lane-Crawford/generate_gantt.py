import csv
from datetime import datetime, timedelta

# Function to check if a date is a weekend
def is_weekend(date):
    return date.weekday() >= 5  # 5 = Saturday, 6 = Sunday

# Function to check if a date is a Hong Kong public holiday
def is_hk_holiday(date):
    holidays = [
        datetime(2026, 1, 1),   # New Year's Day
        datetime(2026, 1, 29),  # Chinese New Year
        datetime(2026, 1, 30),  # Chinese New Year
        datetime(2026, 1, 31),  # Chinese New Year
        datetime(2026, 4, 3),   # Good Friday
        datetime(2026, 4, 4),   # Holy Saturday
        datetime(2026, 4, 6),   # Easter Monday
        datetime(2026, 4, 7),   # Ching Ming Festival
        datetime(2026, 5, 1),   # Labour Day
        datetime(2026, 5, 25),  # Buddha's Birthday
        datetime(2026, 7, 1),   # Hong Kong SAR Establishment Day
        datetime(2026, 9, 16),  # Mid-Autumn Festival
        datetime(2026, 10, 1),  # National Day
    ]
    return date.replace(hour=0, minute=0, second=0, microsecond=0) in holidays

# Read the CSV file
with open('LC3.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Get the header row
header = rows[0]

# Find the start date of the project (Feb 12, 2026)
project_start = datetime(2026, 2, 12)

# Find the end date of the project (latest end date in the CSV)
project_end = project_start
for row in rows[1:]:
    if len(row) >= 6 and row[5]:  # Check if End Date column exists and has a value
        try:
            end_date = datetime.strptime(row[5], '%m/%d/%Y')
            if end_date > project_end:
                project_end = end_date
        except ValueError:
            pass

# Generate all dates from project start to project end
all_dates = []
current_date = project_start
while current_date <= project_end:
    all_dates.append(current_date)
    current_date += timedelta(days=1)

# Create new header with dates
new_header = header[:7]  # Keep the first 7 columns
for date in all_dates:
    new_header.append(date.strftime('%m/%d/%Y'))
new_header.append('Total Work Days')

# Process each row
new_rows = []
new_rows.append(new_header)

for row in rows[1:]:
    if len(row) >= 6 and row[4] and row[5]:  # Check if Start Date and End Date columns exist and have values
        try:
            start_date = datetime.strptime(row[4], '%m/%d/%Y')
            end_date = datetime.strptime(row[5], '%m/%d/%Y')
            
            # Calculate duration in days
            duration = (end_date - start_date).days + 1
            
            # Create new row with the first 6 columns from the original row
            new_row = row[:7]
            if len(new_row) < 7:
                new_row.extend([''] * (7 - len(new_row)))
            
            # Set the duration
            new_row[6] = str(duration)
            
            # Add Gantt chart cells
            work_days = 0
            for date in all_dates:
                if start_date <= date <= end_date:
                    if is_weekend(date) or is_hk_holiday(date):
                        new_row.append('0')
                    else:
                        new_row.append('x')
                        work_days += 1
                else:
                    new_row.append('')
            
            # Add total work days
            new_row.append(str(work_days))
            
            new_rows.append(new_row)
        except ValueError:
            # If there's an error parsing dates, just add the original row
            new_rows.append(row)
    else:
        # If the row doesn't have Start Date or End Date, just add it as is
        new_rows.append(row)

# Write the updated CSV
with open('LC3_updated.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

print("Gantt chart created successfully in LC3_updated.csv")