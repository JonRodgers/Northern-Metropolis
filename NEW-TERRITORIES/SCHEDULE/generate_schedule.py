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

# Hong Kong School Academic Calendar 2026
# Term 1: Early September to mid-November
# Term 2: Late November to early February
# Term 3: Mid-February to late May
# Summer Holiday: June to August
# Christmas Holiday: Late December to early January

school_terms = {
    "Term 1": (datetime(2026, 9, 1), datetime(2026, 11, 15)),
    "Term 2": (datetime(2026, 11, 16), datetime(2027, 2, 5)),
    "Term 3": (datetime(2026, 2, 6), datetime(2026, 5, 31)),
    "Summer Holiday": (datetime(2026, 6, 1), datetime(2026, 8, 31)),
    "Christmas Holiday": (datetime(2026, 12, 19), datetime(2026, 12, 31)),
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
    "AI & Business Development": ["T0101", "T0102", "T0103", "T0104", "T0105", "T0106", "T0107", "T0108", "T0109", "T0110"],
    "BIM & Digital Twin": ["T0201", "T0202", "T0203", "T0204", "T0205", "T0206", "T0207", "T0208", "T0209", "T0210"],
    "Smart Cities & IoT": ["T0301", "T0302", "T0303", "T0304", "T0305", "T0306", "T0307", "T0308", "T0309", "T0310"],
    "Industry 4.0 & Automation": ["T0401", "T0402", "T0403", "T0404", "T0405", "T0406", "T0407", "T0408", "T0409", "T0410"],
    "Programming & Python": ["T0501", "T0502", "T0503", "T0504", "T0505", "T0506", "T0507", "T0508", "T0509", "T0510"],
    "Computational Design": ["T0601", "T0602", "T0603", "T0604", "T0605", "T0606", "T0607", "T0608", "T0609", "T0610"],
    "Standards & Compliance": ["T0701", "T0702", "T0703", "T0704", "T0705", "T0706", "T0707", "T0708", "T0709", "T0710"],
    "Cost, Quantity & Risk Management": ["T0801", "T0802", "T0803", "T0804", "T0805", "T0806", "T0807", "T0808", "T0809", "T0810"],
    "Resource Management & Entrepreneurship": ["T0901", "T0902", "T0903", "T0904", "T0905", "T0906", "T0907", "T0908", "T0909", "T0910"],
    "Drones & Robotics": ["T1001", "T1002", "T1003", "T1004", "T1005", "T1006", "T1007", "T1008", "T1009", "T1010"],
}

def get_term_name(date):
    """Determine which term/holiday period a date falls into"""
    if datetime(2026, 9, 1) <= date <= datetime(2026, 11, 15):
        return "Term 1"
    elif datetime(2026, 11, 16) <= date <= datetime(2027, 2, 5):
        return "Term 2"
    elif datetime(2026, 2, 6) <= date <= datetime(2026, 5, 31):
        return "Term 3"
    elif datetime(2026, 6, 1) <= date <= datetime(2026, 8, 31):
        return "Summer Holiday"
    elif datetime(2026, 12, 19) <= date <= datetime(2026, 12, 31):
        return "Christmas Holiday"
    else:
        return "Holiday"

def get_cell_color(date):
    """Determine cell color: white for normal, light grey for weekends, dark grey for holidays"""
    if date in hk_holidays:
        return "darkgrey"  # Public holiday
    elif date.weekday() >= 5:  # Saturday = 5, Sunday = 6
        return "lightgrey"  # Weekend
    else:
        return "white"  # Normal day

def distribute_classes_for_term(term_name, all_themes):
    """Distribute classes evenly across a term with no repeats"""
    # Create a list of all classes shuffled
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

# Create CSV
with open('schedule.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Header row with dates
    header = ["Time Slot"]
    for date in dates:
        header.append(date.strftime("%a %d-%b"))
    writer.writerow(header)
    
    # Class 1 at 4pm row
    row = ["Class 1 (4pm)"]
    for date in dates:
        term = get_term_name(date)
        color = get_cell_color(date)
        
        if color == "darkgrey":  # Public holiday
            row.append(f"HOLIDAY|{color}")
        elif color == "lightgrey":  # Weekend
            row.append(f"WEEKEND|{color}")
        elif term == "Summer Holiday":
            # Summer camps
            row.append(f"SUMMER CAMP|white")
        elif term == "Christmas Holiday":
            row.append(f"NO CLASS|darkgrey")
        else:
            # Regular term - assign class
            if term in class_index:
                if class_index[term] < len(term_class_distributions[term]):
                    class_id = term_class_distributions[term][class_index[term]]
                    class_index[term] += 1
                    row.append(f"{class_id}|white")
                else:
                    row.append(f"TBD|white")
            else:
                row.append(f"TBD|white")
    writer.writerow(row)
    
    # Reset indices for Class 2
    for term in ["Term 1", "Term 2", "Term 3", "Summer Holiday"]:
        class_index[term] = 0
    
    # Class 2 at 5pm row
    row = ["Class 2 (5pm)"]
    for date in dates:
        term = get_term_name(date)
        color = get_cell_color(date)
        
        if color == "darkgrey":  # Public holiday
            row.append(f"HOLIDAY|{color}")
        elif color == "lightgrey":  # Weekend
            row.append(f"WEEKEND|{color}")
        elif term == "Summer Holiday":
            # Summer camps
            row.append(f"SUMMER CAMP|white")
        elif term == "Christmas Holiday":
            row.append(f"NO CLASS|darkgrey")
        else:
            # Regular term - assign different class
            if term in class_index:
                if class_index[term] < len(term_class_distributions[term]):
                    class_id = term_class_distributions[term][class_index[term]]
                    class_index[term] += 1
                    row.append(f"{class_id}|white")
                else:
                    row.append(f"TBD|white")
            else:
                row.append(f"TBD|white")
    writer.writerow(row)
    
    # Training at 6pm row
    row = ["Training (6pm)"]
    for date in dates:
        term = get_term_name(date)
        color = get_cell_color(date)
        
        if color == "darkgrey":  # Public holiday
            row.append(f"HOLIDAY|{color}")
        elif color == "lightgrey":  # Weekend
            row.append(f"WEEKEND|{color}")
        elif term == "Christmas Holiday":
            row.append(f"NO TRAINING|darkgrey")
        else:
            # Regular term/holiday - assign training
            if term in training_index:
                if training_index[term] < len(term_training_distributions[term]):
                    training_id = term_training_distributions[term][training_index[term]]
                    training_index[term] += 1
                    row.append(f"{training_id}|white")
                else:
                    row.append(f"TBD|white")
            else:
                row.append(f"TBD|white")
    writer.writerow(row)
    
    # Training at 7pm row
    row = ["Training (7pm)"]
    for date in dates:
        term = get_term_name(date)
        color = get_cell_color(date)
        
        if color == "darkgrey":  # Public holiday
            row.append(f"HOLIDAY|{color}")
        elif color == "lightgrey":  # Weekend
            row.append(f"WEEKEND|{color}")
        elif term == "Christmas Holiday":
            row.append(f"NO TRAINING|darkgrey")
        else:
            # Regular term/holiday - assign training
            if term in training_index:
                if training_index[term] < len(term_training_distributions[term]):
                    training_id = term_training_distributions[term][training_index[term]]
                    training_index[term] += 1
                    row.append(f"{training_id}|white")
                else:
                    row.append(f"TBD|white")
            else:
                row.append(f"TBD|white")
    writer.writerow(row)

print("Schedule generated successfully: schedule.csv")
print(f"Date range: {start_date.strftime('%A, %B %d, %Y')} to {end_date.strftime('%A, %B %d, %Y')}")
print(f"Total days: {len(dates)}")
print(f"Public holidays marked: {len(hk_holidays)}")
