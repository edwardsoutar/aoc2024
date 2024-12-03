import os

def parse_reports():
    reports = []

    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    for line in file:
        items = line.split()

        report = []
        for item in items:
            report.append(int(item))

        reports.append(report)

    file.close()

    return reports

def check_dampened_reports_safe(report):
    safe = False

    for i in range(0, len(report)):
        safe |= check_report_safe(report[:i] + report[i+1:])

    return safe

def check_report_safe(report):
    increasing = False

    for i in range(1, len(report)):
        if i == 1:
            increasing = report[i] > report[i-1]

        diff = abs(report[i] - report[i - 1])

        def level_change_safe():
            if diff < 1 or diff > 3:
                return False
            elif increasing and report[i] < report[i - 1]:
                return False
            elif not increasing and report[i] > report[i - 1]:
                return False
            
            return True
        
        if not level_change_safe():
            return False
   
    return True

def count_safe_reports(reports):
    safe_reports_counter = 0

    for report in reports:
        if check_report_safe(report) or check_dampened_reports_safe(report):
            safe_reports_counter += 1

    return safe_reports_counter

reports = parse_reports()

print(count_safe_reports(reports))

