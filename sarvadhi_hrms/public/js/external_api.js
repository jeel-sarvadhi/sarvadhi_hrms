frappe.ui.form.on('Job Applicant', {
    refresh: function(frm) {
        console.log("======",frm)
        frm.add_custom_button('Get IP Info', function() {
            var ip = '8.8.8.8';  // Use dynamic IP if needed
            frappe.call({
                method: 'sarvadhi_hrms.utils.external_api.get_ip_info',
                args: {
                    'ip_address': ip
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(__('IP Info: ') + JSON.stringify(r.message));
                    }
                }
            });
        });
    }
});
