import frappe
import os
import subprocess

@frappe.whitelist()
def bench_migrate():
    # subprocess.run(["bench", "migrate"], check=True)
    os.system('bench migrate')
    # try:
    #     subprocess.run(["bench", "migrate"], check=True)
    #     return "bench migrate done"
    # except subprocess.CalledProcessError as e:
    #     return f"Error occurred during bench migrate: {e}"

@frappe.whitelist()
def bench_build():
    try:
        subprocess.run(["bench", "build"], check=True)
        return "bench migrate successfully"
    except subprocess.CalledProcessError as e:
        return f"Error occurred during bench migrate: {e}"
    # os.system('bench build')

@frappe.whitelist()
def bench_clear_cache():
    try:
        subprocess.run(["bench", "clear-cache"], check=True)
        return "bench clear-cache successfully"
    except subprocess.CalledProcessError as e:
        return f"Error occurred during bench clear-cache: {e}"
    # os.system('bench clear_cache')
    # return "bench_clear_cache"


# @frappe.whitelist()
# def create_new_site(site_name, db_password, admin_password):
#     try:
#         subprocess.run(
#             ["bench", "new-site", site_name, "--db-password", db_password, "--admin-password", admin_password],
#             check=True
#         )
#         return f"New site '{site_name}' created successfully."
#     except subprocess.CalledProcessError as e:
#         return f"Error occurred while creating site '{site_name}': {e}"

@frappe.whitelist()
def create_new_site(site_name, db_password, admin_password):
    
    command = f"bench new-site {site_name} --db-password {db_password} --admin-password {admin_password}"
    
    try:
        exit_code = os.system(command)

        if exit_code == 0:
            return f"New site '{site_name}' created successfully."
        else:
            return f"Error occurred while creating site '{site_name}'. Exit code: {exit_code}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


@frappe.whitelist()
def drop_site(site_name):
    try:
        subprocess.run(["bench", "drop-site", site_name, "--force"], check=True)
        return f"Site '{site_name}' has been successfully dropped."
    except subprocess.CalledProcessError as e:
        return f"Error occurred while dropping site '{site_name}': {e}"
    






