import frappe
import requests
from frappe import _

# api_url = "https://hrms.sarvadhi.work/api/resource/Purchase Receipt"
api_url = "http://localhost:8006/api/resource/Purchase Receipt"

@frappe.whitelist(allow_guest=True)
def post_delivery_note(doc, method):
    """Fetch purchase receipt data via POST request and update the given delivery note."""
    
    
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "token 48f220eb8f94ac7:8385bdd7f2177ea"
        "Authorization": "token 46dcf53cb75edb6:c87cfe265c4cc13"
    }

    try:
        items = []  
        
        for item in doc.items:
            items.append({
                'item_code': item.get('item_code'),
                'qty': item.get('qty'),
                'rate': item.get('rate'),
                'amount': item.get('amount')
            })
        
        post_data = {
            # "supplier": "Neha Patil",
            "supplier": "jeel",
            "items": items
        }

        response = requests.post(api_url, headers=headers, json=post_data)
        
        if response.status_code != 200:
            frappe.log_error(f"Failed to update Delivery Note. API response: {response.text}", "Delivery Note API Error")
        
        if response.status_code == 200:
            frappe.db.commit()
            return _("Delivery Note updated successfully")
        else:
            frappe.throw(_("Failed to update the delivery note. API response: {0}").format(response.text))

    except requests.exceptions.RequestException as e:
        
        frappe.log_error(f"API request failed:", "Delivery Note API Request Exception")
        frappe.throw(_("API request failed:").format(str(e)))
        
    except Exception as e:

        frappe.log_error(f"An error occurred:", frappe.get_traceback())
        frappe.throw(_("An error occurred:").format(str(e)))
