# import requests
# import frappe

# @frappe.whitelist()
# def get_ip_info(ip_address):
#     try:
#         # Replace with the actual IP API URL you want to use
#         api_url = f"http://ip-api.com/json/{ip_address}"
#         frappe.msgprint(":::::::::::::::",api_url)
     
#         # Make a request to the API
#         response = requests.get(api_url)
#         data = response.json()

#         if response.status_code == 200 and data.get('status') == 'success':
#             # Process the data as needed
#             return {
#                 'country': data.get('country'),
#                 'city': data.get('city'),
#                 'region': data.get('regionName'),
#                 'timezone': data.get('timezone'),
#                 'isp': data.get('isp'),
#             }
#         else:
#             return {'error': 'Could not fetch data'}

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), 'IP API Error')
#         return {'error': str(e)}
