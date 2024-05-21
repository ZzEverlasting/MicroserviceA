# MicroserviceA
This is a microservice that converts temperature values from one unit to another. This service utilizes the Flask and Request libraries and is written in Python.

Requirements:
    Python 3+
    Flask Library
    Request Library

Critical --> *Both Libraries Need To Be Installed*

URL can be altered to specification, the default URL is set to 'http://127.0.0.1:5000'.

Microservice utilizes a single ENDPOINT '/convert':
    The use of the POST method converts a temperature unit into another and logs up to 10 previous conversions.
    Converter service takes the input unit and temperature value as well as the output unit for its request body.
    The Converter service responds with converted temperature value and unit as well the log of past conversions.

Example Request:
    import request
    import json

    def convert_temp(set_url, temperature_value, initial_temp_unit, converted_unit):
        url = f'{set_url}/convert'
        payload = {
            "temperature_value" : temperature_value,
            "initial_temp_unit" : initial_temp_unit,
            "converted_unit" : converted_unit
        }
        headers = {'Content-Type:": 'application/json'}
        response = request.post(url, data = json.dumps(payload), headers = headers)
        return response.json
    
    set_url = "http://127.0.0.1:5000"
    temperature_value = 100
    initial_temp_unit = "Celsisus"
    converted_unit = "Fahrenheit"

    result = convert_temp(set_url, temperature_value, initial_temp_unit, converted_unit)
    print(result)

Example Call and Response:
    Creating a JSON payload seen within the "Example Request", calls the POST request for the set_url and sets the
        parameters for the Converter Service to use.
                *** {
                    "temperature_value" = 100,
                    "initial_temp_unit" = "Celsisus,
                    "converted_unit" = "Fahrenheit"
                }

    The Converter Service will respond with a JSON object that prints as such:
        *** {
            "temperature": 212.0 (converted_temp),
            "unit": "Fahrenheit" (converted_unit),
            "log": [
                {"initial_temp_value": 100, "initial_temp_unit": "Celsisus", "converted_temp": 212.0, "converted_unit": "Fahrenheit"}
            ]
        }

To utilize the data used within the Converter Service, save the call function to a variable such as:

        *** "result = convert_temp(set_url, temperature_value, initial_temp_unit, converted_unit)" this saves the conversion data within the result variable
        data within the conversions can be accessed with "result['temperature'], result['unit'], result['log']" for specific data access.

Conversion Log:
    This is included within the '/convert' endpoint for user history and allows the user to see 10 previous conversions.
    If this feature is not needed:

            Exclude the following lines with "-----" on the Converter Service:

            ----# Logs conversion made, up to 10 previous conversions
            ----conversion_log = deque(maxlen=10)

            ----def add_to_log(entry):
            --------conversion_log.append(entry)

            -----log_entry = {
                    'original_temperature': round(temperature_value, 2),
                    'original_unit': initial_temp_unit,
                    'converted_temperature': converted_temp,
                    'converted_unit': converted_unit
                }
            ----add_to_log(log_entry)

            within the return block remove,

                return jsonify({
                    'temperature': converted_temp,
                    'unit': converted_unit,
            --------'log': list(conversion_log)
                })
![Screenshot 2024-05-20 210734](https://github.com/ZzEverlasting/MicroserviceA/assets/110805878/38273e88-2bb1-46c8-875b-849c49b20e8b)

***Identify The Proper URL Within Calling Service for PROPER DEPLOYMENT***

