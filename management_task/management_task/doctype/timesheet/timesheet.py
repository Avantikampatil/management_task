# Copyright (c) 2025, Avantika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Timesheet(Document):
    def on_update(self):
        task_name = self.get("task_name")
        status_name = self.get("status")

        message = f"Task '{task_name}' has been updated with status '{status_name}'"

        frappe.msgprint(message)

    
    def before_save(self):
        self.update_status_on_issue()

    def update_status_on_issue(self):
        frappe.db.set_value("Issue", self.issue , 'status' ,self.status)
        frappe.db.set_value("Task", self.task_name , 'status' ,self.status)


