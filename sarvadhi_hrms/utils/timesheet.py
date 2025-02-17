import frappe
from frappe import _
# from frappe.utils import now_datetime

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



def start_task(timesheet, activity_type, project, task):
    """Start or resume a task inside time_logs in Timesheet."""
    doc = frappe.get_doc("Timesheet", timesheet)

    # Check if a time log already exists with the same activity_type, project, and task
    existing_entry = None
    for entry in doc.time_logs:
        if entry.activity_type == activity_type and entry.project == project and entry.task == task:
            if not entry.to_time:  # If no end time, it's already running
                frappe.throw(f"Task '{task}' is already running.")
            existing_entry = entry
            break

    if existing_entry:
        # Resume the existing entry by creating a new from_time
        new_entry = doc.append("time_logs", {
            "activity_type": activity_type,
            "from_time": now_datetime(),
            "project": project,
            "task": task
        })
    else:
        # Create a fresh time entry if none exists
        new_entry = doc.append("time_logs", {
            "activity_type": activity_type,
            "from_time": now_datetime(),
            "project": project,
            "task": task
        })

    doc.save()
    frappe.db.commit()
    return {"message": "Task Started or Resumed Successfully"}
# ==================


# import frappe
# from frappe.utils import now_datetime, time_diff_in_hours

# def start_task(timesheet, activity_type, project, task):
#     """Start or resume a task inside time_logs in Timesheet."""
#     doc = frappe.get_doc("Timesheet", timesheet)
#     existing_entry = None

#     # Search for an existing entry
#     for entry in doc.time_logs:
#         if entry.activity_type == activity_type and entry.project == project and entry.task == task:
#             existing_entry = entry
#             break

#     if existing_entry:
#         # If already running, show a warning
#         if not existing_entry.to_time:
#             frappe.throw(f"Task '{task}' is already running.")

#         # Resume task by updating to_time and adding hours
#         existing_entry.to_time = now_datetime()
#         new_hours = time_diff_in_hours(existing_entry.to_time, existing_entry.from_time)
#         existing_entry.hours += new_hours

#         frappe.msgprint(f"Task '{task}' resumed. Total Time: {existing_entry.hours:.2f} hours")
#     else:
#         # Create a new time log entry if no existing task
#         doc.append("time_logs", {
#             "activity_type": activity_type,
#             "from_time": now_datetime(),
#             "project": project,
#             "task": task,
#             "hours": 0
#         })

#         frappe.msgprint(f"New Task '{task}' started.")

#     doc.save()
#     frappe.db.commit()
#     return {"message": "Task Started or Resumed Successfully"}
