# Copyright (c) 2025, sarvadhi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.core.doctype.communication.email import make
from frappe.utils import get_url


# class JobOpeningType(Document):
# 	pass

def send_approval_request(doc, method):
    if doc.workflow_state == "Pending":
        approvers = frappe.get_doc("Job Opening Type", doc.custom_job_opening_type) if frappe.db.exists("Job Opening Type", doc.custom_job_opening_type) else None
        
        if not approvers:
            frappe.log_error(
                title="Job Opening Type Not Found",
                message=f"Job Opening Type with name '{doc.custom_job_opening_type}' not found."
            )
            return
        
        # Check if approver is assigned
        if not approvers.approval:
            frappe.log_error(
                title="Approver Not Found",
                message=f"No approver user assigned for Job Opening Type '{doc.custom_job_opening_type}'."
            )
            return
        
        recipient_emails = [approvers.approval]
        
        subject = f"Job Posting Awaiting Approval: {doc.job_title}"
        message = f"""
        <p>Dear Approver,</p>
        <p>A new job posting titled "<strong>{doc.job_title}</strong>" has been created and is awaiting your approval.</p>
        <p>Department: {doc.department}</p>
        <p><a href="{get_url(doc.get_url())}">Click here</a> to review and approve the posting.</p>
        """
        
        # Check if email sending is successful
        email_sent = frappe.sendmail(
            recipients=recipient_emails,
            subject=subject,
            message=message,
            now=True
        )

        if not email_sent:
            frappe.log_error(
                title="Email Sending Failed",
                message=f"Failed to send email to {recipient_emails} for job posting '{doc.name}'."
            )