# Copyright (c) 2025, Avantika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Task(Document):

	

	def on_update(self):
		status_name = self.get("status")
		message = f"Task has been updated with status '{status_name}'"
		frappe.msgprint(message)
		
	