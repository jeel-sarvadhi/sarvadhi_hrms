import frappe
from frappe.utils import getdate, add_days, nowdate, today
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
#     # Fetch the default company for the logged-in user
#     default_company = frappe.defaults.get_defaults().get('company')
    
#     # Fetch the list of active employees with their birthdates, company, and designation
#     birthdays = frappe.get_all("Employee",
#         filters={
#             "company": default_company,
#             "status": "Active",
#         },
#         fields=["name", "employee_name", "date_of_birth", "designation"],
#         order_by="date_of_birth asc"
#     )

#     upcoming_birthdays = []
#     today = getdate(nowdate())  # Get today's date

#     # Loop through the list of employees
#     for emp in birthdays:
#         if emp["date_of_birth"]:
#             # Extract the birthdate, but replace the year to match the current year
#             birth_date = getdate(emp["date_of_birth"]).replace(year=today.year)

#             # Check if the birthday is within the next 30 days
#             if today <= birth_date <= add_days(today, 30):
#                 upcoming_birthdays.append({
#                     "employee_name": emp["employee_name"],
#                     "date_of_birth": birth_date.strftime("%d-%b"),
#                     "day_name": birth_date.strftime("%A"),
#                     "designation": emp['designation']
#                 })

#     return upcoming_birthdays


@frappe.whitelist()
def get_upcoming_holidays():
    """Fetches upcoming holidays from the Holiday List"""
    holiday_list = frappe.get_all("Holiday", 
                                  filters={"holiday_date": [">=", today()]},
                                  fields=["name", "holiday_date", "description"],
                                  order_by="holiday_date asc")
    curr_day = getdate(nowdate())
    upcoming_holidays = []
    
    for holi in holiday_list:
        holiday_date = getdate(holi["holiday_date"]).replace(year=curr_day.year)
        upcoming_holidays.append({
                    "holiday_date": holiday_date.strftime("%d-%b"),
                    "day_name": holiday_date.strftime("%A"),
                    "description": holi.description
                })
    return upcoming_holidays


@frappe.whitelist()
def get_upcoming_birthdayss():
    # Fetch the default company for the logged-in user
    default_company = frappe.defaults.get_defaults().get('company')
    
    # Fetch the list of active employees with their birthdates, company, designation, and image
    birthdays = frappe.get_all("Employee",
        filters={
            "company": default_company,
            "status": "Active",
        },
        fields=["name", "employee_name", "date_of_birth", "designation", "image"],
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
                    "designation": emp['designation'],
                    "image": emp["image"] or "/assets/frappe/images/default-avatar.png"  # Default image if none is set
                })

    return upcoming_birthdays
