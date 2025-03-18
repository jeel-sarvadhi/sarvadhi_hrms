frappe.ui.form.on("Job Offer", {
    job_applicant: function(frm) {
        if (frm.doc.job_applicant) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Job Applicant",
                    name: frm.doc.job_applicant
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("custom_offered_ctc", r.message.custom_current_ctc);
                    }
                }
            });
        }
    }
});


// frappe.ui.form.on("Job Offer", {
//     job_applicant: function(frm) {
//         if (frm.doc.job_applicant) {
//             frappe.call({
//                 method: "frappe.client.get",
//                 args: {
//                     doctype: "Job Applicant",
//                     name: frm.doc.job_applicant
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frm.set_value("custom_compensation_amount", r.message.custom_current_ctc);
//                     }
//                 }
//             });
//         }
//     }
// });