import frappe
import requests
from frappe.utils import validate_email_address
from frappe import _

def on_update_method(doc, method):
    """
    Fetch geolocation data based on the requester's IP and update the Job Applicant document.
    """

    if not doc.email_id or validate_email_address(doc.email_id) is None:
        frappe.throw(_("Invalid email format."))

    # Fetch API Key from System Settings
    api_key = frappe.conf.get("ipapi_access_key")
    if not api_key:
        frappe.throw(_("Missing IP API access key. Please configure it in System Settings."))

    # Get client IP, fallback to default for testing
    client_ip = "122.179.159.67" or frappe.local.request_ip
    url = f"https://api.ipapi.com/{client_ip}?access_key={api_key}&format=1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Map API response data to custom fields
        ip_details = {
            "custom_ip": data.get("ip", "N/A"),
            "custom_ip_type": data.get("type", "N/A"),
            "custom_city": data.get("city", "N/A"),
            "custom_zip_code": data.get("zip", "N/A"),
            "custom_region_name": data.get("region_name", "N/A"),
            "custom_region_code": data.get("region_code", "N/A"),
            "custom_country_name": data.get("country_name", "N/A"),
            "custom_country_code": data.get("country_code", "N/A"),
            "custom_candidate_details": f"""IP: {data.get('ip', '')},
Type: {data.get('type', 'N/A')},
City: {data.get('city', 'N/A')},
Zip Code: {data.get('zip', 'N/A')},
Region Name: {data.get('region_name', 'N/A')},
Region Code: {data.get('region_code', 'N/A')},
Country Name: {data.get('country_name', 'N/A')},
Country Code: {data.get('country_code', 'N/A')}"""
        }

        # Update Job Applicant record
        doc.update(ip_details)
        doc.save()
        frappe.db.commit()

    except requests.exceptions.Timeout:
        frappe.throw(_("Request to IP API timed out."))

    except requests.exceptions.RequestException as e:
        frappe.log_error(str(e), "IP API Request Failed")
        frappe.throw(_("Failed to fetch geolocation data. Please try again later."))

    except Exception as e:
        frappe.log_error(str(e), "Unexpected Error in on_update_method")
        frappe.throw(_("An unexpected error occurred. Please check logs for details."))
