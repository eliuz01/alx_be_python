# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time in "YYYY-MM-DD HH:MM:SS"
    formatted_current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print(f"Current date and time: {formatted_current_datetime}")

def calculate_future_date():
    # Prompt the user to enter a number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        return

    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date in "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future date: {formatted_future_date}")

# Main function to call both display_current_datetime and calculate_future_date
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
