import MES.db as database
import time

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
database.update_order_status(19, 'TBD')
database.update_order_status(47, 'TBD')
database.update_order_status(46, 'TBD')
database.update_order_status(905, 'TBD')
database.update_order_status(18, 'TBD')
non_ordered_orders = database.get_order_status('TBD')
#print(non_ordered_orders)
orders = sorted(non_ordered_orders, key=lambda x: x[5])
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

    # Initialize the latest completion date as the current day
    latest_completion_date = day

    # Keep track of processed order IDs
    processed_order_ids = set()

    # Iterate over each order
    for order in orders:
        # Extract order information
        order_id = order[0]

        # Skip the order if it has already been processed
        if order_id in processed_order_ids:
            continue

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
            earliest_start_date = latest_completion_date  # Set the earliest start date to the latest completion date
        else:
            # Determine the earliest start date for this order based on the earliest start dates for its final products
            earliest_start_date = max(start_dates.values())

        # Calculate the scheduled completion date and quantity for each final product
        for final_product in final_products:
            production_time = suppliers[0].production_time(final_product)

            # Process the quantity in batches
            batch_quantity = quantity

            # If the batch quantity exceeds 4, set it to the exact requested quantity
            if batch_quantity > 4:
                batch_quantity = quantity

            # Accumulate the production time for the entire batch quantity
            total_production_time = production_time * batch_quantity

            # Calculate the completion date for the current batch
            completion_date = earliest_start_date + total_production_time

            # Update the latest completion date if the current completion date is greater
            latest_completion_date = max(latest_completion_date, completion_date)

            # Add the final product information to the master production schedule
            mps.append({
                "order_id": order_id,
                "workpiece": workpiece,
                "final_product": final_product,
                "start_date": earliest_start_date,
                "completion_date": completion_date,
                "quantity": batch_quantity
            })

        # Add the processed order ID to the set
        processed_order_ids.add(order_id)

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


def process_working_orders(stock, orders, day):
    # Define the transformation times for each workpiece
    #Goal piece : transformation pieces, time
    transformation_times = {
        "P3": [("P2", 25)],
        "P4": [("P2", 25)],
        "P5": [("P2", 25), ("P4", 25), ("P7", 25), ("P9", 25)],
        "P6": [("P1", 25)],
        "P7": [("P2", 25), ("P4", 25)],
        "P8": [("P1", 25), ("P6", 60)],
        "P9": [("P2", 25), ("P4", 25), ("P7", 25)]
    }

    # Create an empty list to store the completed transformations
    completed_transformations = []

    # Iterate over the orders
    for order in orders:
        order_id = order[0]
        due_date = order[1]
        quantity = order[4]
        transformed_workpiece = order[3]  # Last transformed workpiece
        status = order[9]
        indexing_workpiece = None
        starting_workpiece = None

        if(status == "IN_PROGRESS"):
            # Find the starting workpiece based on the transformation times
            for indexing_workpiece, transformations in transformation_times.items():
                for transformed_piece, _ in transformations[1]:
                    if transformed_workpiece == indexing_workpiece:
                        starting_workpiece = transformed_piece

                if starting_workpiece is not None:
                    break
                if starting_workpiece is None:
                    continue  # Skip the current order if starting_workpiece is still not assigned
        elif(status == "TBD"):
            # Find the starting workpiece based on the transformation times
            for indexing_workpiece, transformations in transformation_times.items():
                for transformed_piece, _ in transformations:
                    if transformed_workpiece == indexing_workpiece:
                        starting_workpiece = transformed_piece

                if starting_workpiece is not None:
                    break

        # Check if the starting workpiece is in stock
        if database.get_warehouse(starting_workpiece) > 0:
            # Iterate over the transformations for the starting workpiece
            for transformed_piece, time in transformation_times[indexing_workpiece]:
                # Check if there are enough pieces in stock to perform the transformation
                if database.get_warehouse(starting_workpiece) >= 1:
                    # Perform the transformation
                    #database.remove_piece_from_warehouse(starting_workpiece,1)  #RETIRAR DO STOCK
                    #database.add_piece_to_warehouse(transformed_piece,1)  #ADICIONAR STOCK

                    # Add the completed transformation to the list
                    completed_transformations.append(f"{starting_workpiece}_from_{transformed_piece}")

                    # Update the order status
                    if database.get_warehouse(indexing_workpiece) == quantity:
                        print("DONE") #database.update_order_status(order_id, "DONE")
                    else:
                        print("IN_PROGRESS") #database.update_order_status(order_id, "IN_PROGRESS")

                    # Check if the maximum number of transformations for the day has been reached
                    if len(completed_transformations) >= 4:
                        break

        # Check if the maximum number of transformations for the day has been reached
        if len(completed_transformations) >= 4:
            break

    # Add "null" to the completed transformations for any remaining positions
    completed_transformations += ["null"] * (4 - len(completed_transformations))

    return completed_transformations


def process_completed_orders(orders, day):
    completed_orders = []

    # Get the orders with the same due date as the current day
    due_orders = [order for order in orders if order[2] == day]
    stock = database.get_warehouse(None)
    # Check the stock for each due order
    for order in due_orders:
        order_id = order[0]
        workpiece = order[3]
        quantity = order[4]

        # Check if the requested workpiece is in stock and in the correct quantity
        if stock.get(workpiece, 0) >= quantity:
            # Update the stock by deducting the processed quantity
            stock[workpiece] -= quantity

            # Determine the dock number based on the count of strings ending with the number 1
            dock_number = 1 if sum([1 for item in completed_orders if item.endswith("_on_1")]) < 4 else 2

            # Create the tuple and append it to the completed orders list
            completed_orders.append(f"{workpiece}_on_{dock_number}")

    # Fill the remaining positions with "null" if there aren't enough pieces
    remaining_positions = 8 - len(completed_orders)
    completed_orders.extend(["null"] * remaining_positions)

    return completed_orders


def continuous_processing(suppliers):
    while True:
        # Get the current day from the database
        day = database.get_day()
        # Get a new batch of orders
        non_ordered_orders = database.get_order_status('TBD')
        # Sort orders by due date
        orders = sorted(non_ordered_orders, key=lambda x: x[5])

        # Generate the purchasing plan for the day
        purchasing_plan = generate_purchasing_plan(orders, suppliers)

        # Separate the quantities of P1 and P2 from the purchasing plan
        p1_tobuy = purchasing_plan.get("P1", {}).get("Quantity", 0)
        p2_tobuy = purchasing_plan.get("P2", {}).get("Quantity", 0)

        # Generate the master production schedule for the day
        working_orders = generate_mps(orders, suppliers, day)

        # Process the completed orders and determine the delivery orders for the day
        delivery_orders = process_completed_orders(stock, orders, day)

        # Insert the daily plan into the database
        database.add_daily_plan(day, working_orders, delivery_orders, p1_tobuy, p2_tobuy)

        # Wait for 60 seconds before processing the next day
        print("UPDATED")
        time.sleep(60)


def calculo_de_custos(purchasing_plan):
    custofinal = 0
    for workpiece_type, supplier_data in purchasing_plan.items():
        quant = 0
        if workpiece_type in ["P1"]:
            if supplier_data['Supplier'] in ["Supplier A"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant*30
            elif supplier_data['Supplier'] in ["Supplier B"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant * 45
            elif supplier_data['Supplier'] in ["Supplier C"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant * 55
        elif workpiece_type in ["P2"]:
            if supplier_data['Supplier'] in ["Supplier A"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant*10
            elif supplier_data['Supplier'] in ["Supplier B"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant * 15
            elif supplier_data['Supplier'] in ["Supplier C"]:
                quant = supplier_data['Quantity']
                custofinal = custofinal + quant * 18

    return custofinal


def penalty_calc(mps, orders):
    matched_mps = []
    pen = 0

    for mp in mps:
        order_id = mp["order_id"]
        matching_order = None

        for order in orders:
            if isinstance(order, tuple):
                # Handle tuple format where order[0] is the order ID
                if order[0] == order_id:
                    matching_order = order
                    break
            elif isinstance(order, Order):
                # Handle Order object format where order.id is the order ID
                if order.id == order_id:
                    matching_order = order
                    break

        if matching_order:
            if isinstance(matching_order, tuple):
                # Extract attributes from the tuple
                order_id = matching_order[0]
                due_date = matching_order[5]
                late_penalty = matching_order[6]
                early_penalty = matching_order[7]
            elif isinstance(matching_order, Order):
                # Extract attributes from the Order object
                order_id = matching_order.id
                due_date = matching_order.due_date
                late_penalty = matching_order.delay_penalty
                early_penalty = matching_order.advance_penalty

            matched_mp = {
                "order_id": order_id,
                "due_date": due_date,
                "completion_date": mp["completion_date"],
                "late_penalty": late_penalty,
                "early_penalty": early_penalty
            }
            matched_mps.append(matched_mp)

    for matched_mp in matched_mps:
        if matched_mp["completion_date"] == matched_mp["due_date"]:
            pen += 0
        elif matched_mp["completion_date"] < matched_mp["due_date"]:
            numdias = matched_mp["due_date"] - matched_mp["completion_date"]
            pen =pen +  matched_mp["early_penalty"] * numdias
        elif matched_mp["completion_date"] > matched_mp["due_date"]:
            numdias=matched_mp["completion_date"] - matched_mp["due_date"]

            pen =pen + matched_mp["late_penalty"]*numdias

    return pen

day = database.get_day()
stock = database.get_warehouse(None)
mps = generate_mps(orders, suppliers,day)
purchasing_plan = generate_purchasing_plan(orders, suppliers)
custo_final = calculo_de_custos(purchasing_plan)
pen = penalty_calc(mps, orders)

print(process_working_orders(stock, orders, day))
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

print("Penalties:")
print(pen)

print("Suppliers:")
for supplier in suppliers:
    print(supplier.name, supplier.workpiece_types, supplier.min_order, supplier.price_per_piece, supplier.delivery_time)

print("Purchasing Plan:")
for workpiece_type, supplier_data in purchasing_plan.items():
     print("Workpiece Type:", workpiece_type)
     print("Supplier:", supplier_data['Supplier'])
     print("Quantity:", supplier_data['Quantity'])

print("Custo:")
print(custo_final)
a = database.get_order_status('TBD')
#print(a)
#print(database.get_order_status('DONE'))

#print(database.get_order_status('IN_PROGRESS'))



#print(database.get_order_status('DONE'))

id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status = a[0]
#print(id_order)

#continuous_processing(orders)