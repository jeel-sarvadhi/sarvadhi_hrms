app_name = "sarvadhi_hrms"
app_title = "Sarvadhi Hrms"
app_publisher = "sarvadhi"
app_description = "sarvadhi hrms"
app_email = "jeel.k@sarvadhi.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []
fixtures = [
    {"dt": "Document Request", "filters": [], "or_filters": []},
    {"dt": "Custom HTML Block", "filters": [], "or_filters": []},
    {"dt": "Employee Document", "filters": [], "or_filters": []},
    {"dt": "Employee", "filters": [], "or_filters": []},
    {"dt": "Details of Request", "filters": [], "or_filters": []},
    {"dt": "Property Setter", "filters": [["doc_type", "=", "Timesheet"]]},
    # {"dt": "Custom HTML Block", "filters": [
    #     ["name", "in", ["whether updates", "Updates"]]
    # ]}
    {'dt':"Print Format","filters": [["doc_type", "=", "Job Offer"]]}
]
# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sarvadhi_hrms",
# 		"logo": "/assets/sarvadhi_hrms/logo.png",
# 		"title": "Sarvadhi Hrms",
# 		"route": "/sarvadhi_hrms",
# 		"has_permission": "sarvadhi_hrms.api.permission.has_app_permission"
# 	}
# ]


doc_events = {
    "Timesheet": {
        "validate": "sarvadhi_hrms.utils.task_timesheet.validate_timesheet"
    },

    "Job Opening": {
        # "on_update": "sarvadhi_hrms.sarvadhi_hrms.doctype.job_opening_type.job_opening_type.send_approval_request",
        "on_update": "sarvadhi_hrms.utils.email.send_approval_request",
    },

    "Job Applicant": {
        "on_update": "sarvadhi_hrms.utils.job_opening.on_update_method"
    },

    "Delivery Note": {
        "on_submit": "sarvadhi_hrms.utils.delivery_note.post_delivery_note"
    },
    "ToDo": {
        "after_insert": "sarvadhi_hrms.utils.qr_code_generate.custom_generate_qr_code",
    }
}


# override_doctype_class = {
#     "Timesheet": "sarvadhi_hrms.utils.task_timesheet_overrides.CustomTimesheet"
# }


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sarvadhi_hrms/css/sarvadhi_hrms.css"
# app_include_js = "/assets/sarvadhi_hrms/js/sarvadhi_hrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/sarvadhi_hrms/css/sarvadhi_hrms.css"
# web_include_js = "/assets/sarvadhi_hrms/js/sarvadhi_hrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sarvadhi_hrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
# page_js = {
#         "page" : "public/js/external_api.js"
#     }


# include js in doctype views
doctype_js = {"Job Opening": "public/js/job_opening.js",
              "Job Offer": "public/js/job_offer.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sarvadhi_hrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sarvadhi_hrms.utils.jinja_methods",
# 	"filters": "sarvadhi_hrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sarvadhi_hrms.install.before_install"
# after_install = "sarvadhi_hrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sarvadhi_hrms.uninstall.before_uninstall"
# after_uninstall = "sarvadhi_hrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sarvadhi_hrms.utils.before_app_install"
# after_app_install = "sarvadhi_hrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sarvadhi_hrms.utils.before_app_uninstall"
# after_app_uninstall = "sarvadhi_hrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sarvadhi_hrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron": {
        "0/1 * * * *": [
            "sarvadhi_hrms.utils.purchase_api.get_purchase_order"
        ]},
    # 	"all": [
    # 		"sarvadhi_hrms.tasks.all"
    # 	],
    # 	"daily": [
    # 		"sarvadhi_hrms.tasks.daily"
    # 	],
    # 	"hourly": [
    # 		"sarvadhi_hrms.tasks.hourly"
    # 	],
    # 	"weekly": [
    # 		"sarvadhi_hrms.tasks.weekly"
    # 	],
    # 	"monthly": [
    # 		"sarvadhi_hrms.tasks.monthly"
    # 	],
}

# Testing
# -------

# before_tests = "sarvadhi_hrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sarvadhi_hrms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sarvadhi_hrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sarvadhi_hrms.utils.before_request"]
# after_request = ["sarvadhi_hrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["sarvadhi_hrms.utils.before_job"]
# after_job = ["sarvadhi_hrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sarvadhi_hrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
