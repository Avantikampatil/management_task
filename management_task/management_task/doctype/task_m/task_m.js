frappe.ui.form.on('Task_M', {
    refresh: function(frm) {
        // Only allow status updates on submitted tasks (docstatus == 1)
        if (frm.doc.docstatus === 1) {  
            frm.add_custom_button('Update Status', () => {
                // Prompt user to select a new status
                frappe.prompt(
                    [
                        {
                            fieldname: 'new_status',
                            label: 'New Status',
                            fieldtype: 'Select',
                            options: ['Open', 'In Progress', 'Completed', 'Cancelled'],
                            reqd: 1
                        }
                    ],
                    (values) => {
                        // Call the backend to update the status
                        frappe.call({
                            method: 'frappe.client.set_value',
                            args: {
                                doctype: 'Task_M',
                                name: frm.doc.name,
                                fieldname: 'status',
                                value: values.new_status
                            },
                            callback: function(r) {
                                if (!r.exc) {
                                    // Update status and show the message
                                    frappe.msgprint(`Status updated to ${values.new_status}`);
                                    frm.refresh();  // Refresh the form to reflect the status change
                                } else {
                                    // Handle any errors
                                    frappe.msgprint(__('Error in updating the status.'));
                                }
                            }
                        });
                    },
                    'Update Task Status',
                    'Update'
                );
            });
        }
    }
});
