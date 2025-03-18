frappe.ui.form.on('Job Opening', {
    refresh: function(frm) {
        if (frm.doc.custom_publish_on_linkedin) {
            frm.set_value("publish", 1);
        } else {
            frm.set_value("publish", 0);
        }
    },

    custom_publish_on_linkedin: function(frm) {
        if (frm.doc.custom_publish_on_linkedin) {
            frm.set_value("publish", 1);
        } else {
            frm.set_value("publish", 0);
        }
    }
});
