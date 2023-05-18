import MES.db as database


class Order:
    def __init__(self, id, client, order_number, workpiece_type, quantity, due_date, delay_penalty, advance_penalty, path, status):
        self.id = id
        self.client = client
        self.order_number = order_number
        self.workpiece_type = workpiece_type
        self.quantity = quantity
        self.due_date = due_date
        self.delay_penalty = delay_penalty
        self.advance_penalty = advance_penalty
        self.path = path
        self.status = status


class Supplier:
    def __init__(self, name, workpiece_types, min_order, price_per_piece, delivery_time):
        self.name = name
        self.workpiece_types = workpiece_types
        self.min_order = min_order
        self.price_per_piece = price_per_piece
        self.delivery_time = delivery_time

    def can_produce(self, workpiece_type):
        return workpiece_type in self.workpiece_types

    def available_date(self, workpiece_type):
        return self.delivery_time[workpiece_type]

    def production_time(self, workpiece_type):
        return self.delivery_time[workpiece_type]


suppliers = [
    Supplier('Supplier A', ['P1', 'P2'], 16, {'P1': 30, 'P2': 10}, {'P1': 4, 'P2': 4}),
    Supplier('Supplier B', ['P1', 'P2'], 8, {'P1': 45, 'P2': 15}, {'P1': 2, 'P2': 2}),
    Supplier('Supplier C', ['P1', 'P2'], 4, {'P1': 55, 'P2': 18}, {'P1': 1, 'P2': 1})
]

orders = database.get_order(44)
print (orders)


def generate_mps(orders, suppliers):
    # Initialize the master production schedule
    mps = {}

    # Iterate over each order
    for order in orders:
        # Extract order information
        workpiece = orders[3]
        quantity = orders[4]  # Extract the quantity from the order

        # Determine which final products can be made from the ordered workpiece
        if workpiece in ["P6", "P8"]:
            final_products = ["P1"]
        elif workpiece in ["P3", "P4", "P5", "P7", "P9"]:
            final_products = ["P2"]
        else:
            # Skip this order if the workpiece is not valid
            continue

        # Determine the earliest possible start date for each final product based on supplier lead times
        start_dates = {}
        found_start_date = False

        for final_product in final_products:
            can_produce_workpiece = False
            for supplier in suppliers:
                # Check if the supplier can produce the required workpiece
                if supplier.can_produce(workpiece):
                    can_produce_workpiece = True
                    # Calculate the earliest possible start date for this supplier
                    earliest_start_date = max(orders[2] + supplier.delivery_time, supplier.available_date(final_product))

                    # Update the start date for this final product if it is earlier than the current value
                    if final_product not in start_dates or earliest_start_date < start_dates[final_product]:
                        start_dates[final_product] = earliest_start_date
                        found_start_date = True

        # Check if any start dates were recorded
        if not found_start_date:
            earliest_start_date = 0
        else:
            # Determine the earliest start date for this order based on the earliest start dates for its final products
            earliest_start_date = max(start_dates.values())

        # Calculate the scheduled completion date for each final product
        for final_product in final_products:
            completion_date = earliest_start_date + suppliers[0].production_time(final_product)
            # Add/update the final product in the master production schedule
            if final_product not in mps:
                mps[final_product] = {"quantity": quantity, "completion_date": completion_date}
            else:
                # Update the quantity and completion date if needed
                mps[final_product]["quantity"] = max(quantity, mps[final_product]["quantity"])
                mps[final_product]["completion_date"] = max(completion_date, mps[final_product]["completion_date"])

    return mps


def generate_purchasing_plan(mps, suppliers):
    purchasing_plan = {}

    for workpiece_type, data in mps.items():
        quantity = data["quantity"]  # Access the quantity from the data dictionary

        # Determine the appropriate workpiece type to order based on the given workpiece type
        if workpiece_type in ["P6", "P8"]:
            required_workpiece_type = "P1"
        else:
            required_workpiece_type = "P2"

        required_quantity = max(quantity, 4)  # Set the required quantity to at least 4

        # Find the best supplier based on the required quantity
        selected_supplier = None
        for supplier in suppliers:
            if (
                required_workpiece_type in supplier.workpiece_types
                and supplier.min_order <= required_quantity
                and (selected_supplier is None or supplier.min_order > selected_supplier.min_order)
            ):
                selected_supplier = supplier

        # Order the required quantity from the selected supplier
        if selected_supplier is not None:
            purchasing_plan.setdefault(workpiece_type, {})
            purchasing_plan[workpiece_type]['Supplier'] = selected_supplier.name
            purchasing_plan[workpiece_type]['Quantity'] = required_quantity

    return purchasing_plan


mps = generate_mps(orders, suppliers)
purchasing_plan = generate_purchasing_plan(mps, suppliers)


database.create_table("dailyplan")

order = orders  # Since there is only one order, assign it directly to the 'order' variable

workpiece_type = order[3]  # Index 3 corresponds to the 'workpiece_type' in the tuple
quantity = order[4]  # Index 4 corresponds to the 'quantity' in the tuple

for supplier, purchasing_quantity in purchasing_plan.items():
    if workpiece_type in purchasing_quantity:
        # Add a daily plan entry for P1
        if workpiece_type == "P1":
            database.add_daily_plan(order[5], "P1", workpiece_type, purchasing_quantity[workpiece_type], 0)
        # Add a daily plan entry for P2
        elif workpiece_type == "P2":
            database.add_daily_plan(order[5], "P2", workpiece_type, 0, purchasing_quantity[workpiece_type])
        break

print(order[2], order[3], order[4], order[5], order[6], order[7])

# Display the orders, suppliers, MPS, production plan, and purchasing plan
print("Orders:")
print(order[2], order[3], order[4], order[5], order[6], order[7])

print("Suppliers:")
for supplier in suppliers:
    print(supplier.name, supplier.workpiece_types, supplier.min_order, supplier.price_per_piece, supplier.delivery_time)

print("MPS:")
for item, item_data in mps.items():
    print("Item:", item)
    if isinstance(item_data, int):
        print("Quantity:", item_data)
    else:
        print("  Supplier:", item_data.get("Supplier"))
        print("    Quantity:", item_data.get("quantity"))
        print("    Completion Date:", item_data.get("completion_date"))


print("Purchasing Plan:")
for workpiece_type, supplier_data in purchasing_plan.items():
    print("Workpiece Type:", workpiece_type)
    print("Supplier:", supplier_data['Supplier'])
    print("Quantity:", supplier_data['Quantity'])