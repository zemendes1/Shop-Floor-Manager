""""
create_table("orders")
create_table("dailyplan")
create_table("facilities")
create_table("docks")
create_table("day")
create_table("warehouse")


# Testing add_order function
add_order(1, 'Client AA', 18, 'P9', 8, 7, 10, 5, '{1,2,3,4}', 'In Progress')

# Testing add_daily_plan function
add_daily_plan(7, 'orders_9, orders_10', 'P3_from_P2, P3_from_P2, null, null', 75, 100)

# Testing add_facility function
add_facility(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
add_facility(2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
add_facility(3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
add_facility(4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Testing add_dock function
add_dock(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
add_dock(2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#Test Warehouse
add_warehouse(0, 0, 0, 0, 0, 0, 0, 0, 0)

#Test_Updates
update_order(1, 'Client BB', 18, 'P9', 8, 7, 10, 5, '{1,2,3,4}', 'In Progress')
update_daily_plan(7, 'orders_1, orders_2', 'P3_from_P2, P3_from_P2, null, null', 75, 100)
update_facility(4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
update_dock(1, 1, 1, 2, 3, 4, 5, 0, 0, 0)
update_warehouse(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Example get and print get_id_order, get_client, get_ordernumber, get_workpiece, get_quantity, get_duedate,
get_late_penalty, get_early_penalty, get_path, get_status = get_order(1)
print(get_status)
get_date, get_purchase_orders, get_delivery_orders, get_p1_tobuy, get_p2_tobuy = get_daily_plan(7)
print(get_date)
get_num_fac, get_p1_fac, get_p2_fac, get_p3_fac, get_p4_fac, get_p5_fac, get_p6_fac, get_p7_fac, get_p8_fac, get_p9_fac,
get_worktime_fac = get_facility(3)
print(get_p9_fac)
get_num_dock, get_p1_dock, get_p2_dock, get_p3_dock, get_p4_dock, get_p5_dock, get_p6_dock, get_p7_dock, get_p8_dock,
get_p9_dock = get_dock(2)
print(get_p5_dock)
"""