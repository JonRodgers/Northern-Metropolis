import csv
from datetime import datetime, timedelta
import random

# Hong Kong Public Holidays 2026
hk_holidays = {
    datetime(2026, 1, 1): "New Year's Day",
    datetime(2026, 2, 17): "Chinese New Year",
    datetime(2026, 2, 18): "Chinese New Year",
    datetime(2026, 2, 19): "Chinese New Year",
    datetime(2026, 4, 4): "Children's Day",
    datetime(2026, 4, 5): "Ching Ming Festival",
    datetime(2026, 5, 1): "Labour Day",
    datetime(2026, 6, 10): "Dragon Boat Festival",
    datetime(2026, 9, 18): "Day after Mid-Autumn Festival",
    datetime(2026, 10, 1): "National Day",
    datetime(2026, 10, 11): "Chung Yeung Festival",
    datetime(2026, 12, 25): "Christmas Day",
    datetime(2026, 12, 26): "Boxing Day",
}

# Load STEM classes from CSV
stem_classes_dict = {}
with open('../CLASSES/claases.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stem_classes_dict[row['ClassID']] = {
            'name': row['Class Name'],
            'instructor': row['Instructor'],
            'location': row['Location'],
            'capacity': row['Capacity'],
            'theme': row['Theme']
        }

# Load training courses from CSV
training_courses_dict = {}
with open('../TRAINING/training.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        training_courses_dict[row['TrainingID']] = {
            'name': row['Course Name'],
            'instructor': row['Instructor'],
            'location': row['Location'],
            'capacity': row['Capacity'],
            'theme': row['Theme']
        }

# STEM Classes - 10 themes with 10 classes each
stem_classes = {
    "Transportation & Mobility": ["S0101", "S0102", "S0103", "S0104", "S0105", "S0106", "S0107", "S0108", "S0109", "S0110"],
    "Architecture & Structures": ["S0201", "S0202", "S0203", "S0204", "S0205", "S0206", "S0207", "S0208", "S0209", "S0210"],
    "Energy & Power": ["S0301", "S0302", "S0303", "S0304", "S0305", "S0306", "S0307", "S0308", "S0309", "S0310"],
    "Water & Sanitation": ["S0401", "S0402", "S0403", "S0404", "S0405", "S0406", "S0407", "S0408", "S0409", "S0410"],
    "Materials & Manufacturing": ["S0501", "S0502", "S0503", "S0504", "S0505", "S0506", "S0507", "S0508", "S0509", "S0510"],
    "Communication & Information": ["S0601", "S0602", "S0603", "S0604", "S0605", "S0606", "S0607", "S0608", "S0609", "S0610"],
    "Medicine & Health": ["S0701", "S0702", "S0703", "S0704", "S0705", "S0706", "S0707", "S0708", "S0709", "S0710"],
    "Environmental & Sustainability": ["S0801", "S0802", "S0803", "S0804", "S0805", "S0806", "S0807", "S0808", "S0809", "S0810"],
    "Space & Exploration": ["S0901", "S0902", "S0903", "S0904", "S0905", "S0906", "S0907", "S0908", "S0909", "S0910"],
    "Future Technologies & Innovation": ["S1001", "S1002", "S1003", "S1004", "S1005", "S1006", "S1007", "S1008", "S1009", "S1010"],
}

# Training Courses - 10 themes with 10 courses each
training_courses = {
    "AI & Business Development": ["T0101", "T0102", "T0103", "T0104", "T0105", "T0106", "T0107", "T0108", "T0109", "T01010"],
    "BIM & Digital Twin": ["T0201", "T0202", "T0203", "T0204", "T0205", "T0206", "T0207", "T0208", "T0209", "T02010"],
    "Smart Cities & IoT": ["T0301", "T0302", "T0303", "T0304", "T0305", "T0306", "T0307", "T0308", "T0309", "T03010"],
    "Industry 4.0 & Automation": ["T0401", "T0402", "T0403", "T0404", "T0405", "T0406", "T0407", "T0408", "T0409", "T04010"],
    "Programming & Python": ["T0501", "T0502", "T0503", "T0504", "T0505", "T0506", "T0507", "T0508", "T0509", "T05010"],
    "Computational Design": ["T0601", "T0602", "T0603", "T0604", "T0605", "T0606", "T0607", "T0608", "T0609", "T06010"],
    "Standards & Compliance": ["T0701", "T0702", "T0703", "T0704", "T0705", "T0706", "T0707", "T0708", "T0709", "T07010"],
    "Cost, Quantity & Risk": ["T0801", "T0802", "T0803", "T0804", "T0805", "T0806", "T0807", "T0808", "T0809", "T08010"],
    "Resource Management & Entrepreneurship": ["T0901", "T0902", "T0903", "T0904", "T0905", "T0906", "T0907", "T0908", "T0909", "T09010"],
    "Drones & Robotics": ["T1001", "T1002", "T1003", "T1004", "T1005", "T1006", "T1007", "T1008", "T1009", "T10010"],
}

def get_term_name(date):
    """Determine which term/holiday period a date falls into"""
    if datetime(2026, 12, 25) <= date <= datetime(2026, 12, 31):
        return "Christmas Holiday"
    elif datetime(2026, 9, 1) <= date <= datetime(2026, 11, 15):
        return "Term 1"
    elif datetime(2026, 11, 16) <= date <= datetime(2027, 2, 5):
        return "Term 2"
    elif datetime(2026, 2, 6) <= date <= datetime(2026, 5, 31):
        return "Term 3"
    elif datetime(2026, 6, 1) <= date <= datetime(2026, 8, 31):
        return "Summer Holiday"
    else:
        return "Holiday"

def is_weekend(date):
    """Check if date is weekend"""
    return date.weekday() >= 5

def is_holiday(date):
    """Check if date is public holiday"""
    return date in hk_holidays

def distribute_classes_for_term(term_name, all_themes):
    """Distribute classes evenly across a term with no repeats"""
    all_classes = []
    for theme in all_themes:
        all_classes.extend(all_themes[theme])
    random.shuffle(all_classes)
    return all_classes

def distribute_training_for_term(term_name, all_themes):
    """Distribute training courses evenly across a term with no repeats"""
    all_courses = []
    for theme in all_themes:
        all_courses.extend(all_themes[theme])
    random.shuffle(all_courses)
    return all_courses

# Generate schedule
start_date = datetime(2026, 5, 18)  # Monday, May 18, 2026
end_date = datetime(2026, 12, 31)   # December 31, 2026

# Create date range
current_date = start_date
dates = []
while current_date <= end_date:
    dates.append(current_date)
    current_date += timedelta(days=1)

# Prepare class and training distributions for each term
term_class_distributions = {}
term_training_distributions = {}

for term_name in ["Term 1", "Term 2", "Term 3", "Summer Holiday"]:
    term_class_distributions[term_name] = distribute_classes_for_term(term_name, stem_classes)
    term_training_distributions[term_name] = distribute_training_for_term(term_name, training_courses)

# Track which classes/training have been used
class_index = {}
training_index = {}
for term in ["Term 1", "Term 2", "Term 3", "Summer Holiday"]:
    class_index[term] = 0
    training_index[term] = 0

# Create CSV with vertical orientation
with open('schedule.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Header row
    writer.writerow(['Date', 'Day', 'Class 1 (4pm) ID', 'Class 1 Name', 'Class 1 Instructor', 'Class 1 Location', 'Class 1 Capacity',
                     'Class 2 (5pm) ID', 'Class 2 Name', 'Class 2 Instructor', 'Class 2 Location', 'Class 2 Capacity',
                     'Training (6pm) ID', 'Training 6pm Name', 'Training 6pm Instructor', 'Training 6pm Location', 'Training 6pm Capacity',
                     'Training (7pm) ID', 'Training 7pm Name', 'Training 7pm Instructor', 'Training 7pm Location', 'Training 7pm Capacity'])
    
    # Data rows
    for date in dates:
        term = get_term_name(date)
        day_name = date.strftime("%A")
        date_str = date.strftime("%d-%b-%Y")
        
        row = [date_str, day_name]
        
        # Class 1 (4pm)
        if is_holiday(date):
            row.extend(['', '', '', '', ''])
        elif is_weekend(date):
            row.extend(['', '', '', '', ''])
        elif term == "Christmas Holiday":
            row.extend(['', '', '', '', ''])
        else:
            if term in class_index and class_index[term] < len(term_class_distributions[term]):
                class_id = term_class_distributions[term][class_index[term]]
                class_index[term] += 1
                class_info = stem_classes_dict.get(class_id, {})
                row.extend([class_id, class_info.get('name', ''), class_info.get('instructor', ''), 
                           class_info.get('location', ''), class_info.get('capacity', '')])
            else:
                row.extend(['', '', '', '', ''])
        
        # Class 2 (5pm) - reset index for different class
        if is_holiday(date):
            row.extend(['', '', '', '', ''])
        elif is_weekend(date):
            row.extend(['', '', '', '', ''])
        elif term == "Christmas Holiday":
            row.extend(['', '', '', '', ''])
        else:
            if term in class_index and class_index[term] < len(term_class_distributions[term]):
                class_id = term_class_distributions[term][class_index[term]]
                class_index[term] += 1
                class_info = stem_classes_dict.get(class_id, {})
                row.extend([class_id, class_info.get('name', ''), class_info.get('instructor', ''), 
                           class_info.get('location', ''), class_info.get('capacity', '')])
            else:
                row.extend(['', '', '', '', ''])
        
        # Training (6pm)
        if is_holiday(date):
            row.extend(['', '', '', '', ''])
        elif is_weekend(date):
            row.extend(['', '', '', '', ''])
        elif term == "Christmas Holiday":
            row.extend(['', '', '', '', ''])
        else:
            if term in training_index and training_index[term] < len(term_training_distributions[term]):
                training_id = term_training_distributions[term][training_index[term]]
                training_index[term] += 1
                training_info = training_courses_dict.get(training_id, {})
                row.extend([training_id, training_info.get('name', ''), training_info.get('instructor', ''), 
                           training_info.get('location', ''), training_info.get('capacity', '')])
            else:
                row.extend(['', '', '', '', ''])
        
        # Training (7pm)
        if is_holiday(date):
            row.extend(['', '', '', '', ''])
        elif is_weekend(date):
            row.extend(['', '', '', '', ''])
        elif term == "Christmas Holiday":
            row.extend(['', '', '', '', ''])
        else:
            if term in training_index and training_index[term] < len(term_training_distributions[term]):
                training_id = term_training_distributions[term][training_index[term]]
                training_index[term] += 1
                training_info = training_courses_dict.get(training_id, {})
                row.extend([training_id, training_info.get('name', ''), training_info.get('instructor', ''), 
                           training_info.get('location', ''), training_info.get('capacity', '')])
            else:
                row.extend(['', '', '', '', ''])
        
        writer.writerow(row)

print("Vertical schedule generated successfully: schedule.csv")
print(f"Date range: {start_date.strftime('%A, %B %d, %Y')} to {end_date.strftime('%A, %B %d, %Y')}")
print(f"Total days: {len(dates)}")
print(f"Public holidays marked: {len(hk_holidays)}")
print(f"Format: Vertical with dates as rows, class/training details in columns")
