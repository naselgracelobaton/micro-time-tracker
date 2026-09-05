import csv
import os
from datetime import datetime


print("Daily time tracking")
print("Enter the hours worked for this session:")
hours = float(input()) 
print("Enter the minutes worked for this session:")
minutes = float(input())

print("Task name:") 
task_name = input()
print("Quantity of tasks completed:")
tasks_completed = int(input())  

print(f"Session Summary:")  
print(f"Task: {task_name}")
print(f"Time worked: {hours} hours and {minutes} minutes")
print(f"Tasks completed: {tasks_completed}")

total_time = hours + (minutes / 60)
print(f"Total time worked in hours: {total_time:.2f} hours")    
rate_per_hour = 420
earnings = total_time * rate_per_hour
print(f"Earnings for this session: P {earnings:.2f}")

from datetime import datetime
today = datetime.now().strftime("%B %d, %Y - %A")    
print(f"Date: {today}")

# save to file

CSV_FILE = "TIMETRACKING.csv"
def save_to_csv(task_name, hours, minutes, tasks_completed, total_time, earnings, today):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        #header kung wala pang file

        if not file_exists:
            writer.writerow(["Task Name", "Hours Worked", "Minutes Worked", "Tasks Completed", "Total Time (hours)", "Earnings (P)", "Date"])

            date = datetime.now().strftime("%B %d, %Y - %A")

            writer.writerow([task_name, hours, minutes, tasks_completed, total_time, earnings, today])

save_to_csv(task_name, hours, minutes, tasks_completed, total_time, earnings, today)

print("Session data saved to TIMETRACKING.txt")