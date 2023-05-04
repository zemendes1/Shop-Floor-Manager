import receive_xml
import MES.db as database




class Order:
    def __init__(self, order_number, workpiece_type, quantity, due_date, delay_penalty, advance_penalty):
        self.order_number = order_number
        self.workpiece_type = workpiece_type
        self.quantity = quantity
        self.due_date = due_date
        self.delay_penalty = delay_penalty
        self.advance_penalty = advance_penalty


orders = []


class Supplier:
    def __init__(self, name, workpiece_types, min_order, price_per_piece, delivery_time):
        self.name = name
        self.workpiece_types = workpiece_types
        self.min_order = min_order
        self.price_per_piece = price_per_piece
        self.delivery_time = delivery_time



# create a new instance of the Xml class
xml = receive_xml.Xml("127.0.0.1", 54321)

# receive the data from the UDP socket
if xml.xml2string():
    # extract the order values from the XML data
    xml.get_order()

    # access the order values using the instance attributes
    for i in range(xml.i):
        order_number = xml.number[i]
        workpiece_type = xml.workpiece[i]
        quantity = xml.quantity[i]
        due_date = xml.duedate[i]
        delay_penalty = xml.latepen[i]
        advance_penalty = xml.earlypen[i]

        order = Order(order_number, workpiece_type, quantity, due_date, delay_penalty, advance_penalty)
        orders.append(order)

        # do something with the order values here
        print(f"Order {order_number}: {quantity} units of {workpiece_type} due on {due_date}")
else:
    print("Failed to receive data from UDP socket")


suppliers = [
    Supplier('Supplier A', ['P1', 'P2'], 16, {'P1': 30, 'P2': 10}, {'P1': 4, 'P2': 4}),
    Supplier('Supplier B', ['P1', 'P2'], 8, {'P1': 45, 'P2': 15}, {'P1': 2, 'P2': 2}),
    Supplier('Supplier C', ['P1', 'P2'], 4, {'P1': 55, 'P2': 18}, {'P1': 1, 'P2': 1})
]


def generate_mps(orders, suppliers):
    # Initialize the master production schedule
    mps = {}

    # Iterate over each order
    for order in orders:
        # Extract order information
        name, order_num, workpiece, qty, due_date, delay_penalty, advance_penalty = order

        # Determine which final products can be made from the ordered workpiece
        if workpiece == "P1":
            final_products = ["P6", "P8"]
        elif workpiece == "P2":
            final_products = ["P3", "P4", "P5", "P7", "P9"]
        else:
            # Skip this order if the workpiece is not valid
            continue

        # Determine the earliest possible start date for each final product based on supplier lead times
        start_dates = {}
        for final_product in final_products:
            for supplier in suppliers:
                # Check if the supplier can produce the required workpiece
                if supplier.can_produce(workpiece):
                    # Calculate the earliest possible start date for this supplier
                    earliest_start_date = max(order_num + supplier.delivery_time, supplier.available_date(final_product))

                    # Update the start date for this final product if it is earlier than the current value
                    if final_product not in start_dates or earliest_start_date < start_dates[final_product]:
                        start_dates[final_product] = earliest_start_date

        # Determine the earliest start date for this order based on the earliest start dates for its final products
        earliest_start_date = max(start_dates.values())

        # Calculate the scheduled completion date for each final product
        for final_product in final_products:
            completion_date = earliest_start_date + suppliers[0].production_time(final_product)
            if final_product in mps and completion_date > mps[final_product]:
                # Skip this order if it cannot be completed before the currently scheduled completion date for this final product
                continue

            # Add the final product to the master production schedule
            mps[final_product] = completion_date

    return mps


def generate_production_plan(mps):
    production_plan = {}
    for item, item_data in mps.items():
        if item in ["P6", "P8"]:
            p1_qty = item_data["quantity"]
            production_plan[item] = {"P1": p1_qty}
        else:
            p2_qty = item_data["quantity"]
            p3_qty = round(p2_qty * 0.5)
            p4_qty = round(p2_qty * 0.3)
            p5_qty = round(p2_qty * 0.2)
            p7_qty = round(p2_qty * 0.8)
            p9_qty = round(p2_qty * 0.4)
            production_plan[item] = {"P2": p2_qty, "P3": p3_qty, "P4": p4_qty,
                                     "P5": p5_qty, "P7": p7_qty, "P9": p9_qty}
    return production_plan


def generate_purchasing_plan(mps):
    purchasing_plan = {}
    for item, item_data in mps.items():
        for supplier, supplier_data in item_data["suppliers"].items():
            supplier_p1_qty = 0
            supplier_p2_qty = 0
            supplier_qty = 0
            if item == "P1":
                supplier_p1_qty = item_data["quantity"]
                supplier_qty = supplier_p1_qty
            elif item == "P2":
                supplier_p2_qty = item_data["quantity"]
                supplier_qty = supplier_p2_qty
            purchasing_plan.setdefault(supplier, {})
            purchasing_plan[supplier].setdefault("P1", 0)
            purchasing_plan[supplier].setdefault("P2", 0)
            if supplier_data["supplies"]["P1"] and supplier_p1_qty > 0:
                # Check if supplier can supply P1 and if order quantity meets minimum order
                if supplier_p1_qty < supplier_data["min_order"]:
                    supplier_p1_qty = supplier_data["min_order"]
                purchasing_plan[supplier]["P1"] += supplier_p1_qty
                supplier_qty -= supplier_p1_qty
            if supplier_data["supplies"]["P2"] and supplier_p2_qty > 0:
                # Check if supplier can supply P2 and if order quantity meets minimum order
                if supplier_p2_qty < supplier_data["min_order"]:
                    supplier_p2_qty = supplier_data["min_order"]
                purchasing_plan[supplier]["P2"] += supplier_p2_qty
                supplier_qty -= supplier_p2_qty
            if supplier_qty > 0:
                # If there is still quantity left to be ordered, order additional minimum orders
                for initial_piece in ["P1", "P2"]:
                    if supplier_data["supplies"][initial_piece]:
                        min_order = supplier_data["min_order"]
                        while supplier_qty >= min_order:
                            purchasing_plan[supplier][initial_piece] += min_order
                            supplier_qty -= min_order
    return purchasing_plan


mps = generate_mps(orders, suppliers)
production_plan = generate_production_plan(mps)
purchasing_plan = generate_purchasing_plan(mps)


database.create_table("dailyplan")

# loop through the orders and add a daily plan entry for each one
for order in orders:
    workpiece_type = order.workpiece_type
    quantity = order.quantity
    purchasing_quantity = purchasing_plan[workpiece_type]
    production_quantity = production_plan[workpiece_type]

    # add a daily plan entry for P1
    if workpiece_type == "P1":
        database.add_daily_plan(order.due_date,
                                                 purchasing_quantity,
                                                 production_quantity,
                                                 purchasing_quantity,
                                                 0)
    # add a daily plan entry for P2
    elif workpiece_type == "P2":
        database.add_daily_plan(order.due_date,
                                                 purchasing_quantity,
                                                 production_quantity,
                                                 0,
                                                 purchasing_quantity)


# Display the orders, suppliers, MPS, production plan, and purchasing plan
print("Orders:")
for order in orders:
    print(order.order_number, order.workpiece_type, order.quantity, order.due_date, order.delay_penalty, order.advance_penalty)

print("Suppliers:")
for supplier in suppliers:
    print(supplier.name, supplier.workpiece_types, supplier.min_order, supplier.price_per_piece, supplier.delivery_time)

print("MPS:")
for item, item_data in mps.items():
    print("Item:", item)
    for supplier, supplier_data in item_data["suppliers"].items():
        print("  Supplier:", supplier)
        print("    Quantity:", supplier_data["quantity"])
        print("    Supplies P1:", supplier_data["supplies"]["P1"])
        print("    Supplies P2:", supplier_data["supplies"]["P2"])

print("Production Plan:")
for workpiece_type, quantity in production_plan.items():
    print("Workpiece Type:", workpiece_type)
    print("Quantity:", quantity)

print("Purchasing Plan:")
for supplier, supplier_data in purchasing_plan.items():
    print("Supplier:", supplier)
    for workpiece_type, quantity in supplier_data.items():
        print("  Workpiece Type:", workpiece_type)
        print("  Quantity:", quantity)