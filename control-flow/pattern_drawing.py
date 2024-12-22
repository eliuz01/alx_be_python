# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to print each row of the pattern
while row < size:
    # Use a for loop to print the asterisks in each row
    for col in range(size):
        print("*", end="")
    # After printing one row, go to the next line
    print()
    # Increment the row counter
    row += 1
