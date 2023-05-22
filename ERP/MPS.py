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

orders = database.get_order_status('TBD')
#print(orders)


def generate_mps(orders, suppliers, day):
    # Initialize the master production schedule
    mps = []

    # Define the production times for each workpiece
    production_times = {
        "P3": 25,
        "P4": 25,
        "P5": 75,
        "P6": 60,
        "P7": 60,
        "P8": 80,
        "P9": 60
    }

    # Iterate over each order
    for order in orders:
        # Extract order information
        order_id = order[0]
        workpiece = order[3]
        quantity = order[4]  # Extract the quantity from the order

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
                    earliest_start_date = max(order[2] + supplier.delivery_time, supplier.available_date(final_product))

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

        # Calculate the scheduled completion date and quantity for each final product
        for final_product in final_products:
            production_time = suppliers[0].production_time(final_product)
            num_days = quantity // 4  # Calculate the number of full production days
            remaining_quantity = quantity % 4  # Calculate the remaining quantity after full production days

            # Distribute the quantity over the production days
            completion_date = earliest_start_date
            for _ in range(num_days):
                completion_date += 1  # Increment the completion date by 1 day
                completion_date += day  # Add the current value of day to the completion date
                # Add the final product information to the master production schedule

                completion_date += production_times[workpiece]  # Add the production time for the workpiece
                mps.append({
                    "order_id": order_id,
                    "workpiece": workpiece,
                    "start_date": earliest_start_date,
                    "completion_date": completion_date,
                    "quantity": quantity
                })

            # Add the remaining quantity to the last production day
            if remaining_quantity > 0:
                completion_date += 1
                completion_date += day  # Add the current value of day to the completion date

                completion_date += production_times[workpiece] * remaining_quantity  # Add the production time for the remaining quantity
                mps.append({
                    "order_id": order_id,
                    "workpiece": workpiece,
                    "start_date": earliest_start_date,
                    "completion_date": completion_date,
                    "quantity": remaining_quantity
                })

    return mps


def generate_purchasing_plan(orders, suppliers):
    purchasing_plan = {}

    # Collect the quantities of required workpieces P1 and P2 from the orders
    for order in orders:
        workpiece_type = order[3]
        quantity = order[4]

        # Determine the appropriate workpiece type to order based on the given workpiece type
        if workpiece_type in ["P6", "P8"]:
            required_workpiece_type = "P1"
        else:
            required_workpiece_type = "P2"

        # Add the quantity to the purchasing plan for the corresponding workpiece type
        purchasing_plan.setdefault(required_workpiece_type, 0)
        purchasing_plan[required_workpiece_type] += quantity

    # Adjust the quantity to ensure a minimum order quantity of 4 units
    for workpiece_type in purchasing_plan.keys():
        purchasing_plan[workpiece_type] = max(purchasing_plan[workpiece_type], 4)

    # Determine the supplier for each workpiece type based on the minimum order quantity
    for workpiece_type, quantity in purchasing_plan.items():
        selected_supplier = None
        for supplier in suppliers:
            if (
                workpiece_type in supplier.workpiece_types
                and supplier.min_order <= quantity
                and (selected_supplier is None or supplier.min_order > selected_supplier.min_order)
            ):
                selected_supplier = supplier

        # Add the supplier information to the purchasing plan
        if selected_supplier is not None:
            purchasing_plan[workpiece_type] = {
                "Supplier": selected_supplier.name,
                "Quantity": quantity
            }
        else:
            # If no supplier is found, remove the workpiece type from the purchasing plan
            del purchasing_plan[workpiece_type]

    return purchasing_plan


day = database.get_day()
stock = database.get_warehouse(None)
mps = generate_mps(orders, suppliers,day)

purchasing_plan = generate_purchasing_plan(orders, suppliers)
print("mps:", mps)  # Add this line to print the entire mps list

database.create_table("dailyplan")

order = orders  # Since there is only one order, assign it directly to the 'order' variable

workpiece_type = order[3]  # Index 3 corresponds to the 'workpiece_type' in the tuple
quantity = order[4]  # Index 4 corresponds to the 'quantity' in the tuple
for i in range(1):
    for data in mps:
        workpiece_typee = data["workpiece"]
        quantity = data["quantity"]
        order_id = data["order_id"]
        date = data["completion_date"]
        #print(workpiece_typee)
        #print(quantity)
        #print(order_id)
        #print(date)
        #database.add_daily_plan(day, f"{workpiece_typee} from P2","null",
        #                        0, 8)
        if workpiece_type in purchasing_plan:
            print(workpiece_type)
            # Add a daily plan entry for P1
            if workpiece_type in ["P6", "P8"]:
                database.add_daily_plan(date, f"orders_{order_id}", f"{workpiece_type} from P1",
                                        purchasing_plan[workpiece_type], 0)
                print(f"orders_{order_id}")
                # Add a daily plan entry for P2
            elif workpiece_type in ["P3", "P4", "P5", "P7", "P9"]:
                database.add_daily_plan(date, f"orders_{order_id}", f"{workpiece_type} from P2",
                                        purchasing_plan[workpiece_type], 0)
                print(f"orders_{order_id}")
    break

# Print the values inside the mps dictionary
for order in mps:
    order_id = order["order_id"]
    workpiece = order["workpiece"]
    start_date = order["start_date"]
    completion_date = order["completion_date"]
    quantity = order["quantity"]

    print(f"Order ID: {order_id}")
    print(
        f"Workpiece: {workpiece} | Start Date: {start_date} | Completion Date: {completion_date} | Quantity: {quantity}")
    print("------------------")

print("Suppliers:")
for supplier in suppliers:
    print(supplier.name, supplier.workpiece_types, supplier.min_order, supplier.price_per_piece, supplier.delivery_time)

print("Purchasing Plan:")
for workpiece_type, supplier_data in purchasing_plan.items():
     print("Workpiece Type:", workpiece_type)
     print("Supplier:", supplier_data['Supplier'])
     print("Quantity:", supplier_data['Quantity'])

a = database.get_order_status('TBD')
#print(a)
#print(database.get_order_status('DONE'))

#print(database.get_order_status('IN_PROGRESS'))

database.update_order_status(906, 'DONE')

#print(database.get_order_status('DONE'))

id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status = a[0]
#print(id_order)