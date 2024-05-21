import requests
import json

def convert_temperature(temperature_value, initial_temp_unit, converted_unit):
    url = 'http://127.0.0.1:5000/convert'
    payload = {
        "temperature": temperature_value,
        "initial_temp_unit": initial_temp_unit,
        "converted_unit": converted_unit
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

def print_conversion_log(log):
    print("\nConversion Log (last 10 conversions):")
    for entry in log:
        print(f"{entry['original_temperature']} {entry['original_unit']} -> {entry['converted_temperature']} {entry['converted_unit']}")

def main():
    print("Temperature Conversion App")
    print("==========================")
    valid_units = {"Celsius", "Fahrenheit", "Kelvin"}
    
    while True:
        initial_temp_unit = input("\nEnter the unit of the input temperature (Celsius, Fahrenheit, Kelvin): ").capitalize()
        if initial_temp_unit not in valid_units:
            print("Invalid unit. Please enter a valid unit (Celsius, Fahrenheit, Kelvin).")
            continue
        
        try:
            temperature_value = float(input(f"Enter the temperature value in {initial_temp_unit}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        converted_unit = input("Enter the target unit for conversion (Celsius, Fahrenheit, Kelvin): ").capitalize()
        if converted_unit not in valid_units:
            print("Invalid unit. Please enter a valid unit (Celsius, Fahrenheit, Kelvin).")
            continue

        result = convert_temperature(temperature_value, initial_temp_unit, converted_unit)
        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print(f"\nConverted {temperature_value} {initial_temp_unit} to {result['temperature']} {converted_unit}")
            print_conversion_log(result["log"])

        another = input("\nDo you want to perform another conversion? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == '__main__':
    main()
