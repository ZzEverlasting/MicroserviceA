from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__)

# Conversion functions, results are rounded to two decimal points.
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

def celsius_to_kelvin(celsius):
    return round(celsius + 273.15, 2)

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def fahrenheit_to_kelvin(fahrenheit):
    return round(celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit)), 2)

def kelvin_to_fahrenheit(kelvin):
    return round(celsius_to_fahrenheit(kelvin_to_celsius(kelvin)), 2)

# Logs conversion made, up to 10 previous conversions
conversion_log = deque(maxlen=10)      ###Remove if log is not needed

def add_to_log(entry):                  ###Remove if log is not needed
    conversion_log.append(entry)        ###Remove if log is not needed

# Helper function to validate and convert temperature
def convert_temperature(temperature_value, initial_temp_unit, converted_unit):
    if initial_temp_unit == 'celsius':
        if converted_unit == 'fahrenheit':
            return celsius_to_fahrenheit(temperature_value)
        elif converted_unit == 'kelvin':
            return celsius_to_kelvin(temperature_value)
    elif initial_temp_unit == 'fahrenheit':
        if converted_unit == 'celsius':
            return fahrenheit_to_celsius(temperature_value)
        elif converted_unit == 'kelvin':
            return fahrenheit_to_kelvin(temperature_value)
    elif initial_temp_unit == 'kelvin':
        if converted_unit == 'celsius':
            return kelvin_to_celsius(temperature_value)
        elif converted_unit == 'fahrenheit':
            return kelvin_to_fahrenheit(temperature_value)
    return None

@app.route('/convert', methods=['POST'])
def convert_temperature_route():
    data = request.get_json()
    if 'temperature' not in data or 'initial_temp_unit' not in data or 'converted_unit' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        temperature_value = float(data['temperature'])
    except ValueError:
        return jsonify({'error': 'Temperature must be a number'}), 400

    initial_temp_unit = data['initial_temp_unit'].lower()
    converted_unit = data['converted_unit'].lower()
    
    converted_temp = convert_temperature(temperature_value, initial_temp_unit, converted_unit)
    if converted_temp is None:
        return jsonify({'error': 'Unknown unit'}), 400
    
    log_entry = {                                   ###Remove if log is not needed
        'original_temperature': round(temperature_value, 2),        
        'original_unit': initial_temp_unit,
        'converted_temperature': converted_temp,
        'converted_unit': converted_unit
    }
    add_to_log(log_entry)                           ###Remove if log is not needed
    
    return jsonify({
        'temperature': converted_temp,
        'unit': converted_unit,
        'log': list(conversion_log)                 ###Remove if log is not needed
    })

if __name__ == '__main__':
    app.run(debug=False)
