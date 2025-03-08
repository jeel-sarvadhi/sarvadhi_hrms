# import frappe
# import requests

# @frappe.whitelist()
# def get_job_opening(docname):

#     # ip_response = frappe.local.request_ip
#     # print("Public IP address:", ip_response)

#     url = "https://api.ipapi.com/122.179.159.67?access_key=f06eb2a8f1fd13c197749760ca8313b0&format=1"

#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()

#         ip = data.get('ip','')
#         ip_type = data.get('type', 'N/A')
#         city = data.get('city', 'N/A')
#         zip_code = data.get('zip', 'N/A')
#         region_name = data.get('region_name', 'N/A')
#         region_code = data.get('region_code', 'N/A')
#         country_name = data.get('country_name', 'N/A')
#         country_code = data.get('country_code', 'N/A')

#         try:
#             job_applicant = frappe.get_doc("Job Applicant", docname)

#             job_applicant.custom_ip = ip
#             job_applicant.custom_ip_type = ip_type
#             job_applicant.custom_city = city
#             job_applicant.custom_zip_code = zip_code
#             job_applicant.custom_region_name = region_name
#             job_applicant.custom_region_code = region_code
#             job_applicant.custom_country_name = country_name
#             job_applicant.custom_country_code = country_code
#             job_applicant.custom_candidate_details = f"IP: {ip}, Type: {ip_type}"

#             job_applicant.save()
#             frappe.db.commit()

#             return {"job_applicant": job_applicant.as_dict(), "message": "Job Applicant updated with geolocation data."}

#         except frappe.DoesNotExistError:
#             return {"error": f"Job Applicant with email {docname} does not exist."}

#     else:
#         return {"error": f"Failed to fetch data. Status code: {response.status_code}"}


import frappe
import requests
from frappe.utils import validate_email_address
from frappe import _


@frappe.whitelist()
def get_job_opening(docname: str):
    """
    Fetch geolocation data based on the requester's IP and update the Job Applicant document.
    """

    if not docname or not validate_email_address(docname):
        return {"error": _("Invalid email format.")}

    api_key = frappe.conf.get("ipapi_access_key")
    if not api_key:
        return {"error": _("Missing IP API access key. Please configure it in site_config.json.")}

    # client_ip = frappe.local.request_ip or "122.179.159.67"
    client_ip = "122.179.159.67" or frappe.local.request_ip
    url = f"https://api.ipapi.com/{client_ip}?access_key={api_key}&format=1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        ip_details = {
            "custom_ip": data.get("ip", ""),
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

        job_applicant = frappe.get_doc("Job Applicant", {"email_id": docname})

        job_applicant.update(ip_details)
        job_applicant.save()
        frappe.db.commit()

        return {"job_applicant": job_applicant.as_dict(), "message": _("Job Applicant updated successfully.")}

    except frappe.DoesNotExistError:
        return {"error": _(f"Job Applicant with email {docname} does not exist.")}

    except requests.exceptions.Timeout:
        return {"error": _("Request to IP API timed out.")}

    except requests.exceptions.RequestException as e:
        frappe.log_error(message=str(e), title="IP API Request Failed")
        return {"error": _("Failed to fetch geolocation data. Please try again later.")}

    except Exception as e:
        frappe.log_error(message=str(
            e), title="Unexpected Error in get_job_opening")
        return {"error": _("An unexpected error occurred. Please check logs for details.")}


