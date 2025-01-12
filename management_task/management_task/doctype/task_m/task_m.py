import frappe
from frappe.model.document import Document

class Task_M(Document):
    def validate(self):
        # Ensure priority is valid (before submitting)
        if self.priority not in ['High', 'Medium', 'Low']:
            frappe.throw("Priority must be 'High', 'Medium', or 'Low'")

    def on_submit(self):
        # Set default status on submission
        if not self.status:
            self.status = 'Open'  # Default to Open when the task is submitted
        frappe.msgprint(f"Task '{self.name}' has been submitted with status: {self.status}")

    def update_status(self, new_status):
        # Allow status update only for submitted tasks (docstatus == 1)
        if self.docstatus != 1:
            frappe.throw("Task must be submitted to update the status.")
        
        # Update the status and save the task (removing validation for allowed statuses)
        self.status = new_status
        self.save(ignore_permissions=True)
        frappe.msgprint(f"Task '{self.name}' status updated to {new_status}")

    def on_update(self):
        # Logic to be triggered after the task is updated
        # For example, log the update or send a notification
        frappe.msgprint(f"Task '{self.name}' has been updated.")
        # You can perform additional actions here, such as logging, notifying users, etc.
