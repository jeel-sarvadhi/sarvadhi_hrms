frappe.ui.form.on('Job Applicant', {
    // Trigger after save
    before_save: function(frm) {
        console.log(frm,"-------"); // Log the form object to the console for debugging
        
        // Call the server-side method to fetch geolocation data and update the Job Applicant
        frappe.call({
            method: 'sarvadhi_hrms.utils.job_opening_utils.get_job_opening',
            args: {
                docname: frm.doc.name  // Pass the docname (email or ID) of the Job Applicant
            },
            callback: function(response) {
                console.log(response);  // Check the whole response in the console
                if (response.message) {
                    console.log('API Data Fetched Successfully');
                    // If needed, you can also show a message in the UI:
                    frappe.msgprint('API Data Fetched Successfully');
                } else {
                    console.log('Failed to fetch API Data');
                    frappe.msgprint('Failed to fetch API Data');
                }
            },
            error: function(err) {
                console.error('Error calling the API:', err);
                frappe.msgprint('Error occurred while calling the API');
            }
        });
    }
});
