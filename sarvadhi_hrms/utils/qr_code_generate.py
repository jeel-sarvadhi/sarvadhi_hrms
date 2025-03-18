import frappe
import requests
import frappe.utils

def custom_generate_qr_code(doc, method):

    doc_url = frappe.utils.get_url(doc.doctype, doc.name)
    print(":::::::::::::::::::::",doc_url)
    qr_code_url = f"https://api.dub.co/qr?url={doc_url}"
    
    try:
        response = requests.get(qr_code_url)
        
        if response.status_code == 200:
            
            file_content = response.content
            file_name = f"QR_Code_{doc.name}.png"
            file_doc = frappe.get_doc({
                "doctype": "File",
                "file_name": file_name,
                "attached_to_doctype": doc.doctype,
                "attached_to_name": doc.name,
                "content": file_content
            })
            file_doc.save()
            print(f"QR Code generated and saved successfully for {doc.name}")
        
        else:
            frappe.msgprint(f'Failed to create QR Code. Status Code: {response.status_code}')
    
    except Exception as e:
        frappe.log_error(f"Error while generating QR code for {doc.name}: {str(e)}", "QR Code Generation Error")
        frappe.msgprint(f"An error occurred while generating the QR code: {str(e)}")
