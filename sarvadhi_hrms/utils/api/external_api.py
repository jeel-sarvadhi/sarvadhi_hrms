import frappe
# import requests
# import json

@frappe.whitelist()
def say_hello():
    return "hello"

@frappe.whitelist()
def job_applicant_api():
    data=frappe.request.get_json()

    for new_data in data:
        existing_applicant = frappe.db.get_value('Job Applicant', {'email_id': new_data.get('email_id')}, 'name')

        if existing_applicant:
            print(f"Duplicate entry found for {new_data.get('email_id')}.")
        else:
            applicant_data = frappe.get_doc({
                'doctype': 'Job Applicant',
                'applicant_name': new_data.get('applicant_name'),
                'email_id': new_data.get('email_id')
            })
            applicant_data.insert()

    frappe.db.commit()


@frappe.whitelist(allow_guest=True)
def dynamic_api():
    """Design and implement a dynamic API"""
    try:
        data = frappe.request.get_json()
        print("Received data:", data)
        
        doc_type = data.get('doctype')
        body_data = data.get('data', [])
        
        if not isinstance(body_data, list):
            frappe.local.response['http_status_code'] = 400
            return {'Error': 'Provided data is not in list format'}
        
        if not doc_type or not body_data:
            frappe.local.response['http_status_code'] = 400
            return {'Error': 'Missing "doctype" or "data" in the request'}
        
        meta = frappe.get_meta(doc_type)
        required_fields = [field.fieldname for field in meta.fields if field.reqd]
        
        for new_data in body_data:
            missing_fields = [field for field in required_fields if field not in new_data or not new_data.get(field)]
            
            if missing_fields:
                frappe.local.response['http_status_code'] = 400
                return {'Error': f'Missing required fields: {", ".join(missing_fields)}'}

            doc_data = { 'doctype': doc_type, **new_data }
            try:
                new_doc = frappe.get_doc(doc_data)
                print("Document Data:", new_doc)
                new_doc.insert()
                frappe.db.commit()

            except Exception as insert_error:
                if 'No doctype' in str(insert_error):
                    print(f"Module import failed: {insert_error}")
    
                    frappe.local.response['http_status_code'] = 400
                    return {
                        'Error': f"Failed to insert document: Module import failed for {doc_type}, the DocType you're trying to open might be deleted. Error: {insert_error}"
                    }
                else:
                    print(f"Error inserting document: {insert_error}")
                    frappe.local.response['http_status_code'] = 500  
                    return {'Error': f'Failed to insert document: {str(insert_error)}'}
                
        frappe.local.response['http_status_code'] = 201  
        return {'Success': 'Data Entry created successfully'}

    except Exception as e:
        frappe.db.rollback()
        frappe.local.response['http_status_code'] = 500
        print(f"Error: {str(e)}")
        return {'Error': f'An error occurred: {str(e)}'}

