file_name ="input.txt"

def is_safe_report(report):
    report_size = len(report)
    is_increasing = False
    is_decreasing = False

    if report[0] < report[1] and abs(report[0] - report[1]) <= 3: # Compares adjacent data to determine initial trend
        is_increasing = True
    elif report[0] > report[1] and abs(report[0] - report[1]) <= 3:
        is_decreasing = True
    else:
        return False

    for i in range(report_size - 1): # Checks data for safety based on trend
        if is_increasing:
            if report[i] >= report[i + 1] or abs(report[i] - report[i + 1]) > 3:
                return False
        if is_decreasing:
            if report[i] <= report[i + 1] or abs(report[i] - report[i + 1]) > 3:
                return False

    return True

with open(file_name) as file:
    # Read lines and process them
    list_of_reports = [list(map(int, line.split())) for line in file]

safe_reports = 0
unsafe_reports = []

for report in list_of_reports:
    if is_safe_report(report):
        safe_reports += 1
    else:
        unsafe_reports.append(report) # List of reports unsafe before dampening

dampened_safe_reports = 0

for report in unsafe_reports: 
        report_size = len(report)

        for i in range(report_size): # Brute force, remove one by one data element from report and check for safety
            modified_report = report[:i] + report[i + 1:]  # Remove current element

            if is_safe_report(modified_report): 
                dampened_safe_reports += 1
                break  # Stop checking after finding a valid dampened report
        
        
print(f"There are {safe_reports} safe reports!")
print(f"There are {dampened_safe_reports + safe_reports} safe reports after dampening!")