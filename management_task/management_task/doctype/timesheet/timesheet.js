// Copyright (c) 2025, Avantika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Timesheet", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Timesheet', {
    setup: function (frm) {
        frm.set_query('issue', function () {
            return {
                filters: [
                    ['Issue', 'project', '=', frm.doc.project]
            ],
            };
        });
    },
         
});