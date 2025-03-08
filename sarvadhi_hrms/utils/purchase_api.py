import frappe
import requests
from frappe.utils import today


@frappe.whitelist(allow_guest=True)
def get_purchase_order():
    """call api and get purchase order data and integrate with selling order"""

    api = 'https://hrms.sarvadhi.work/api/resource/Purchase%20Order?fields=["total_qty","name"]'

    headers = {
        "Content-Type": "application/json",
        'Authorization': 'token 48f220eb8f94ac7:8385bdd7f2177ea'
    }

    response = requests.get(api, headers=headers)
    data = response.json()
    if "data" not in data:
        return("API response does not contain 'data'.")
        
    purchase_orders = data["data"]

    create_sales_orders = []

    for purchase_order in purchase_orders:
        existing_sales_order = frappe.get_all('Sales Order', filters={'po_no': purchase_order.get('name')})
        if existing_sales_order:
            frappe.msgprint(f"Sales Order already exists for Purchase Order: {purchase_order.get('name')}.")
            continue
        sales_order = frappe.new_doc("Sales Order")
        sales_order.customer = 'Harsh Vadhiya'
        sales_order.po_no = purchase_order.get('name', '')
        
        sales_order.delivery_date = purchase_order.get(
            'schedule_date', today())

        sales_order.currency = 'INR'
        sales_order.selling_price_list = 'Standard Selling'
        sales_order.set_warehouse = 'Work In Progress - S'
        sales_order.status = 'Draft'
        print(":::::::::::",purchase_order)
        item = {
            'item_code': 'ITEM-001',
            'qty': purchase_order.get('total_qty')
        }

        sales_order.append('items', item)

        sales_order.insert()
        frappe.db.commit()

        create_sales_orders.append(sales_order)

    return create_sales_orders
