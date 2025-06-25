import re

def write_report(message: str):
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def parse_time(t):
    hour, min = map(int, t.split(':'))
    return hour * 60 + min

def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()
    return lines

def process_day(lines, activity_totals):
    entries = []
    for line in lines:
        match = re.match(r'(\d{2}:\d{2}) (.+)', line)
        if match:
            time, activity = match.groups()
            entries.append((time, activity))
    for i in range(len(entries)-1):
        start, activity = entries[i]
        end, _ = entries[i+1]
        start_min = parse_time(start)
        end_min = parse_time(end)
        duration = end_min - start_min
        if activity in activity_totals:
            activity_totals[activity] += duration
        else:
            activity_totals[activity] = duration
        write_report(f"{start}-{end} {activity}")

def print_summary(activity_totals):
    total = sum(activity_totals.values())
    for activity in sorted(activity_totals):
        minutes = activity_totals[activity]
        percent = int(round(100 * minutes / total))
        write_report(f"{activity:<25}{minutes:<4} minutes   {percent:>2}%")

def main():
    file_name = "timelog.log"
    lines = open_file(file_name)
    days = []
    day = []
    # Dividing into different days
    for line in lines:
        if line.strip() == "":
            if day:
                days.append(day)
                day = []
        else:
            day.append(line)
    if day:
        days.append(day)

    activity_totals = {}
    for day in days:
        process_day(day, activity_totals)
        write_report("")
    print_summary(activity_totals)

if __name__== "__main__":
    main()