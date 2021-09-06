import json
from os import read, write

def read_data(file_name):
    fd = open(file_name,'r')
    re = fd.read()
    fd.close()
    record = json.loads(re)
    return record

def write_data(file_name,json_data):
    fd = open(file_name,'w')
    fd.write(json_data)
    fd.close()


def add_item_into_inventory(data):
    name_of_prod = input("Enter Product name:")
    price = int(input("Enter Price of product:"))
    quantity = int(input("enter Quantity:"))
    manufacture_date=input("enter manufacture date:")
    company_name=input("enter company name:")
    expiry_date=input("enter expiry date:")
    data[name_of_prod] = {"price" : price, "quantity":quantity, "manufacture_date":manufacture_date, "company_name":company_name, "expiry_date":expiry_date}
    json_data = json.dumps(data)
    write_data('inventory_data.json',json_data)
    

def add_to_inventory():
    number = int(input("enter the number of data available:"))
    existing_data = read_data('inventory_data.json')
    for i in range(number):
        add_item_into_inventory(existing_data)


def clear_inventory():
    data = "{}"
    write_data('inventory_data.json',data)

def clear_sales_data():
    data = "{}"
    write_data('sales.json',data)

def add_customer_order(customer_id):
    prod_name = input("Enter Product name:")
    #check_product_availability(prod_name)
    quan = int(input("Enter Quantity:"))
    check_quantity_availability(prod_name,quan)
    customer_order = {"prod_name": prod_name, "quantity":quan}
    existing_customer_data = read_data('sales.json')
    existing_customer_data[customer_id] = {}
    existing_customer_data[customer_id] = customer_order
    json_data = json.dumps(existing_customer_data)   
    write_data('sales.json',json_data)
    update_inventory_data(prod_name,quan)

def check_quantity_availability(product_name,required_quantity):
    existing_inventory_data = read_data("inventory_data.json")
    check_product_availability(product_name)
    if required_quantity > existing_inventory_data[product_name]['quantity'] :
        print("Required quantity is not available")
        take_customer_order()

def check_product_availability(prod_name):
    existing_inventory_data = read_data("inventory_data.json")
    available_products = list(existing_inventory_data.keys())
    if available_products.count(prod_name) ==0:
        print("Product is Not available")
        take_customer_order()

def update_inventory_data(product_name, quantity_purchased):
    existing_inventory_data = read_data("inventory_data.json")
    existing_inventory_data[product_name]['quantity'] = existing_inventory_data[product_name]['quantity'] - quantity_purchased
    json_data = json.dumps(existing_inventory_data)
    write_data('inventory_data.json',json_data)



def take_customer_order():
    available_customer_data = read_data('sales.json')
    customer_ids = list(available_customer_data.keys())
    cust_id = len(customer_ids)+1
    add_customer_order(cust_id)

def calculate_bill(customer_id):
    sales_data = read_data('sales.json')
    inventory_data = read_data('inventory_data.json')
    bill_amount = sales_data[customer_id]['quantity'] * inventory_data[sales_data[customer_id]['prod_name']]['price']
    print(bill_amount)
    update_amount_in_sales(bill_amount,customer_id)


def update_amount_in_sales(amount,customer_id):
    sales_data = read_data('sales.json')
    sales_data[customer_id]['amount'] = amount
    json_data = json.dumps(sales_data)
    write_data('sales.json',json_data)



def todo_action():
    action = int(input("1. Update Inventor\n2. Take Order\n3. Clear inventory\n4. Clear sales data\n5. Calculate Bill\nEnter Action Number:"))
    if action == 1:
        add_to_inventory()
    elif action == 2:
        take_customer_order()
    elif action == 3:
        clear_inventory()
    elif action == 4:
        clear_sales_data()
    elif action == 5:
        cust_id = input("Enter Customer ID:")
        calculate_bill(cust_id)

    else:
        print("Enter a valid action\n")
        todo_action()

todo_action()
























    

