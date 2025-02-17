// frappe.ui.form.on('Timesheet', {
// 	refresh(frm) {
// 		// your code here
// 	}
// })

frappe.ui.form.on('Timesheet', {
    // Trigger validation when the form is being saved
    validate: function(frm) {
        // Make sure the task field is filled
        if (frm.doc.task) {
            // Check if there is already an active timesheet for the same task
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Timesheet',
                    filters: {
                        task: frm.doc.task,
                        status: 'Draft'  // Check if there is any active timesheet with status 'Open'
                    },
                    fields: ['name'],
                    limit_page_length: 1  // Only need to check for the first active timesheet
                },
                callback: function(response) {
                    if (response.message && response.message.length > 0) {
                        // Show an error message if an active timesheet exists
                        frappe.msgprint(__('You already have an active timesheet for this task. Please stop the current one before creating a new one.'));
                        // Prevent form submission by returning false
                        frappe.validated = false;
                    }
                }
            });
        }
    }
});
