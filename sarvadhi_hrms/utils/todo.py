import frappe
from frappe.utils import getdate, add_days, nowdate
# from frappe.model.document import Document

@frappe.whitelist()
def get_todo():
    username = frappe.session.user  # Get the logged-in user's name

    # Fetch the roles assigned to the user
    user_roles = [role.role for role in frappe.get_all('Has Role', fields=['role'], filters={'parent': username})]

    # Get all ToDo tasks for the user, based on their roles
    todos = frappe.get_all('ToDo', filters={
        'owner': username,
    }, fields=['name', 'date', 'priority', 'status', 'owner'])
    print("==================================",todos)
    return todos

# @frappe.whitelist()
# def get_upcoming_birthdays():
#     today = getdate()
#     upcoming_birthday_date = add_days(today, 30)  # Change the number to specify the window
#     birthdays = frappe.get_all('Employee', filters={'date_of_birth': ('between', [today, upcoming_birthday_date])},
#                                fields=['name', 'date_of_birth'])
#     return birthdays


@frappe.whitelist()
def get_upcoming_birthdays():
    # Fetch the default company for the logged-in user
    default_company = frappe.defaults.get_defaults().get('company')
    
    # Fetch the list of active employees with their birthdates, company, and designation
    birthdays = frappe.get_all("Employee",
        filters={
            "company": default_company,
            "status": "Active",
        },
        fields=["name", "employee_name", "date_of_birth", "designation"],
        order_by="date_of_birth asc"
    )

    upcoming_birthdays = []
    today = getdate(nowdate())  # Get today's date

    # Loop through the list of employees
    for emp in birthdays:
        if emp["date_of_birth"]:
            # Extract the birthdate, but replace the year to match the current year
            birth_date = getdate(emp["date_of_birth"]).replace(year=today.year)

            # Check if the birthday is within the next 30 days
            if today <= birth_date <= add_days(today, 30):
                upcoming_birthdays.append({
                    "employee_name": emp["employee_name"],
                    "date_of_birth": birth_date.strftime("%d-%b"),
                    "day_name": birth_date.strftime("%A"),
                    "designation": emp['designation']
                })

    return upcoming_birthdays

