import requests
import frappe
import json


@frappe.whitelist()
def job_applicant():
    data=frappe.request.get_json()
    # a=frappe.request.get_data()
    print(data,":::::::::::::::")

    for new_data in data:
        existing_applicant = frappe.db.get_value('Job Applicant', {'email_id': new_data.get('email_id')}, 'name')
        print("=========================",existing_applicant)

        if existing_applicant:
            print(f"Duplicate entry found for {new_data.get('email_id')}.")
        else:
            applicant_data = frappe.get_doc({
                'doctype': 'Job Applicant',
                'applicant_name': new_data.get('applicant_name'),
                'email_id': new_data.get('email_id')
            })
            applicant_data.insert()
            print(":::::::::::::::::::::", applicant_data)

    frappe.db.commit()



