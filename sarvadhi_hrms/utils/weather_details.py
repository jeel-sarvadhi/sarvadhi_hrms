# import frappe
# import requests

# @frappe.whitelist(allow_guest=True)
# def get_weather_details(location="Surat"):
#     # Use your actual weather API key here
#     api_key = "72fa3296bca44b0ba8764614250303"
#     weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    
#     try:
#         response = requests.get(weather_url)
#         data = response.json()
        
#         if response.status_code == 200:
#             weather_info = {
#                 "location": data.get('name'),
#                 "temperature": data['main']['temp'],
#                 "description": data['weather'][0]['description'],
#                 "humidity": data['main']['humidity']
#             }
#             return weather_info
#         else:
#             return {"error": "Unable to fetch weather details"}
#     except Exception as e:
#         return {"error": f"Error: {str(e)}"}


import frappe
import requests

@frappe.whitelist(allow_guest=True)
def get_weather_details(location="Surat"):
    # Use your actual weather API key here
    api_key = "72fa3296bca44b0ba8764614250303"
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    
    try:
        response = requests.get(weather_url)
        data = response.json()
        
        if response.status_code == 200:
            # Accessing the correct fields based on WeatherAPI response
            weather_info = {
                "location": data['location']['name'],
                "temperature": data['current']['temp_c'],  # Corrected to temp_c for Celsius
                "description": data['current']['condition']['text'],  # Accessing weather description
                "humidity": data['current']['humidity']  # Corrected to humidity
            }
            return weather_info
        else:
            return {"error": "Unable to fetch weather details"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}



