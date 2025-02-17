import frappe
from frappe import _

def validate_timesheet(doc, method):
    """ Prevents creating a new Timesheet if an employee has a Draft Timesheet """

    filters = {
        "employee": doc.employee,
        "status": "Draft"
    }

    # Exclude the current Timesheet being validated
    if doc.name:
        filters["name"] = ("!=", doc.name)  

    existing_timesheet = frappe.get_all(
        "Timesheet",
        filters=filters,
        fields=["name"],  # Fetch the existing timesheet name
        limit=1
    )

    if existing_timesheet:
        timesheet_name = existing_timesheet[0]["name"]
        frappe.throw(
            _("Employee {0} already has an existing Timesheet in 'Draft' status ({1}). "
              "Please submit or cancel it before creating a new one.")
            .format(doc.employee, timesheet_name)
        )
