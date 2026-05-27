import csv
from datetime import datetime, timedelta
import random

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

# Summer camp periods (between school terms)
summer_camps = [
    ("Summer Camp 1", datetime(2026, 6, 1), datetime(2026, 8, 31)),  # June 1 - Aug 31 (summer break)
]

def is_weekend(date):
    """Check if date is weekend"""
    return date.weekday() >= 5

def is_public_holiday(date):
    """Check if date is public holiday"""
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
    return date in hk_holidays

def get_camp_name(date):
    """Determine which summer camp period a date falls into"""
    for camp_name, start, end in summer_camps:
        if start <= date <= end:
            return camp_name
    return None

def distribute_classes_for_camp(all_themes):
    """Distribute classes for camp with no repeats"""
    all_classes = []
    for theme in all_themes:
        all_classes.extend(all_themes[theme])
    random.shuffle(all_classes)
    return all_classes

def distribute_training_for_camp(all_themes):
    """Distribute training courses for camp with no repeats"""
    all_courses = []
    for theme in all_themes:
        all_courses.extend(all_themes[theme])
    random.shuffle(all_courses)
    return all_courses

# Generate summer camp schedule
start_date = datetime(2026, 6, 1)
end_date = datetime(2026, 8, 31)

# Create date range for summer camps
current_date = start_date
dates = []
while current_date <= end_date:
    dates.append(current_date)
    current_date += timedelta(days=1)

# Prepare class and training distributions for summer camps
camp_class_distributions = distribute_classes_for_camp(stem_classes)
camp_training_distributions = distribute_training_for_camp(training_courses)

class_index = 0
training_index = 0

# Create CSV for summer camps
with open('summer_camps.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Header row
    writer.writerow(['Date', 'Day', 
                     'Class 1 (9am) ID', 'Class 1 Name', 'Class 1 Instructor', 'Class 1 Location', 'Class 1 Capacity',
                     'Class 2 (10am) ID', 'Class 2 Name', 'Class 2 Instructor', 'Class 2 Location', 'Class 2 Capacity',
                     'Class 3 (11am) ID', 'Class 3 Name', 'Class 3 Instructor', 'Class 3 Location', 'Class 3 Capacity',
                     'Class 4 (12pm) ID', 'Class 4 Name', 'Class 4 Instructor', 'Class 4 Location', 'Class 4 Capacity',
                     'Training 1 (2pm) ID', 'Training 1 Name', 'Training 1 Instructor', 'Training 1 Location', 'Training 1 Capacity',
                     'Training 2 (3pm) ID', 'Training 2 Name', 'Training 2 Instructor', 'Training 2 Location', 'Training 2 Capacity',
                     'Training 3 (4pm) ID', 'Training 3 Name', 'Training 3 Instructor', 'Training 3 Location', 'Training 3 Capacity',
                     'Training 4 (5pm) ID', 'Training 4 Name', 'Training 4 Instructor', 'Training 4 Location', 'Training 4 Capacity'])
    
    # Data rows
    for date in dates:
        day_name = date.strftime("%A")
        date_str = date.strftime("%d-%b-%Y")
        camp_name = get_camp_name(date)
        
        row = [date_str, day_name]
        
        # Check if it's a weekend or holiday
        if is_weekend(date) or is_public_holiday(date):
            # Empty row for weekends and holidays
            row.extend([''] * 32)  # 32 columns for all classes and training
        elif camp_name:
            # Summer camp day - add 4 STEM classes
            for i in range(4):
                class_id = camp_class_distributions[class_index % len(camp_class_distributions)]
                class_index += 1
                class_info = stem_classes_dict.get(class_id, {})
                row.extend([class_id, class_info.get('name', ''), class_info.get('instructor', ''),
                           class_info.get('location', ''), class_info.get('capacity', '')])
            
            # Add 4 AECO training sessions
            for i in range(4):
                training_id = camp_training_distributions[training_index % len(camp_training_distributions)]
                training_index += 1
                training_info = training_courses_dict.get(training_id, {})
                row.extend([training_id, training_info.get('name', ''), training_info.get('instructor', ''),
                           training_info.get('location', ''), training_info.get('capacity', '')])
        else:
            # Not a summer camp day
            row.extend([''] * 32)
        
        writer.writerow(row)

print("Summer camps schedule generated successfully: summer_camps.csv")
print(f"Date range: {start_date.strftime('%A, %B %d, %Y')} to {end_date.strftime('%A, %B %d, %Y')}")
print(f"Total days: {len(dates)}")
print(f"Format: Vertical with dates as rows, 4 STEM classes (9am-12pm) and 4 training sessions (2pm-5pm)")
