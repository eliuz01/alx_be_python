# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for converting Celsius to Fahrenheit

# Global Offsets
FAHRENHEIT_OFFSET = 32
CELSIUS_OFFSET = 0

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Conversion formula: (Fahrenheit - 32) * (5 / 9)
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Conversion formula: Celsius * (9 / 5) + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET
    return fahrenheit

# Function to handle user input and perform conversion
def temperature_conversion():
    try:
        # Prompt the user to enter a temperature value
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt the user to specify whether it's in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

# Main function to start the program
if __name__ == "__main__":
    temperature_conversion()
