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

with open("TIMETRACKING.txt", "a") as file:
    file.write(f"Date: {today}\n")
    file.write(f"Task: {task_name}\n")
    file.write(f"Time worked: {hours} hours and {minutes} minutes\n")
    file.write(f"Tasks completed: {tasks_completed}\n")
    file.write(f"Total time worked in hours: {total_time:.2f} hours\n")
    file.write(f"Earnings for this session: P {earnings:.2f}\n")
    file.write("\n")  # Add a newline for separation between sessions
print("Session data saved to TIMETRACKING.txt")
