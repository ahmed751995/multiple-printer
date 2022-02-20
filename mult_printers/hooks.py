from . import __version__ as app_version

app_name = "mult_printers"
app_title = "Mult Printers"
app_publisher = "Ahmed Abdulrahman"
app_description = "send print order to multible printers"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ahmed751995"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mult_printers/css/mult_printers.css"
# app_include_js = "/assets/mult_printers/js/mult_printers.js"

# include js, css files in header of web template
# web_include_css = "/assets/mult_printers/css/mult_printers.css"
# web_include_js = "/assets/mult_printers/js/mult_printers.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mult_printers/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mult_printers.install.before_install"
# after_install = "mult_printers.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mult_printers.uninstall.before_uninstall"
# after_uninstall = "mult_printers.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mult_printers.notifications.get_notification_config"

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

doc_events = {
	"POS Invoice": {
		"on_submit": "mult_printers.send_to_printers.send_to_printers",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mult_printers.tasks.all"
# 	],
# 	"daily": [
# 		"mult_printers.tasks.daily"
# 	],
# 	"hourly": [
# 		"mult_printers.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mult_printers.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mult_printers.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mult_printers.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mult_printers.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mult_printers.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mult_printers.auth.validate"
# ]

