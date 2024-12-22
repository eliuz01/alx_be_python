# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using Match Case
match priority:
    case 'high':
        priority_message = "high priority task"
    case 'medium':
        priority_message = "medium priority task"
    case 'low':
        priority_message = "low priority task"
    case _:
        priority_message = "task with unknown priority"

# Modify reminder based on whether the task is time-bound
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

# Print the customized reminder message
print(f"Reminder: '{task}' is a {priority_message} {time_message}")
