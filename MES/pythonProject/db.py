import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminadmin",
    database="test"
)

mycursor = mydb.cursor()


def create_table(_table):
    # CREATE TABLE
    create_script = ""
    if _table == "orders":
        create_script = " CREATE TABLE IF NOT EXISTS orders (" \
                        "id INT PRIMARY KEY," \
                        "Client varchar(40) NOT NULL," \
                        "OrderNumber INT," \
                        "WorkPiece varchar(40) NOT NULL," \
                        "Quantity INT," \
                        "DueDate INT," \
                        "Late_Penalty INT," \
                        "Early_Penalty INT," \
                        "path varchar(40)," \
                        "status varchar(40) NOT NULL" \
                        ");"

    elif _table == "dailyPlan":
        create_script = "CREATE TABLE IF NOT EXISTS dailyPlan (" \
                        "date DATE PRIMARY KEY," \
                        "Purchase_orders varchar(40)," \
                        "Delivery_orders varchar(40), " \
                        "P1_toBuy INT CHECK (P1_toBuy >= 0)," \
                        "P2_toBuy INT CHECK (P2_toBuy >= 0)" \
                        ");"

    elif _table == "facilities":
        create_script = "CREATE TABLE IF NOT EXISTS facilities (" \
                        "num INT PRIMARY KEY," \
                        "P1 INT CHECK (P1 >= 0)," \
                        "P2 INT CHECK (P2 >= 0)," \
                        "P3 INT CHECK (P3 >= 0)," \
                        "P4 INT CHECK (P4 >= 0)," \
                        "P5 INT CHECK (P5 >= 0)," \
                        "P6 INT CHECK (P6 >= 0)," \
                        "P7 INT CHECK (P7 >= 0)," \
                        "P8 INT CHECK (P8 >= 0)," \
                        "P9 INT CHECK (P9 >= 0)," \
                        "workTime INT" \
                        ");"

    elif _table == "docks":
        create_script = "CREATE TABLE IF NOT EXISTS docks (" \
                        "num INT PRIMARY KEY," \
                        "P1 INT CHECK (P1 >= 0)," \
                        "P2 INT CHECK (P2 >= 0)," \
                        "P3 INT CHECK (P3 >= 0)," \
                        "P4 INT CHECK (P4 >= 0)," \
                        "P5 INT CHECK (P5 >= 0)," \
                        "P6 INT CHECK (P6 >= 0)," \
                        "P7 INT CHECK (P7 >= 0)," \
                        "P8 INT CHECK (P8 >= 0)," \
                        "P9 INT CHECK (P9 >= 0)" \
                        ");"
    mycursor.execute(create_script)
    mydb.commit()


def add_order(id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status):
    new_order = "INSERT INTO orders" \
                " (id, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status)" \
                " VALUES ({}, '{}', {}, '{}', {}, {}, {}, {}, '{}', '{}');".format(id_order, client, ordernumber,
                                                                                   workpiece,
                                                                                   quantity, duedate, late_penalty,
                                                                                   early_penalty, path, status)

    mycursor.execute(new_order)
    mydb.commit()
    return 0


def get_order(id_order):
    query = "SELECT * FROM orders WHERE id= {}".format(id_order)
    mycursor.execute(query)
    order_values = mycursor.fetchone()
    mydb.commit()
    return order_values


def add_daily_plan(date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy):
    new_plan = "INSERT INTO dailyplan" \
               " (date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy)" \
               " VALUES ('{}', '{}', '{}', {}, {});".format(date, purchase_orders, delivery_orders, p1_tobuy,
                                                            p2_tobuy)
    mycursor.execute(new_plan)
    mydb.commit()
    return 0


def get_daily_plan(date):
    query = "SELECT * FROM dailyplan WHERE date = '{}'".format(date)
    mycursor.execute(query)
    daily_plan_values = mycursor.fetchone()
    mydb.commit()
    return daily_plan_values


def add_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    new_facility = "INSERT INTO facilities" \
                   " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9, worktime)" \
                   " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8,
                                                                                  p9, work_time)
    mycursor.execute(new_facility)
    mydb.commit()
    return 0


def get_facility(num):
    query = "SELECT * FROM facilities WHERE num = {}".format(num)
    mycursor.execute(query)
    facility_values = mycursor.fetchone()
    mydb.commit()
    return facility_values


def add_dock(num, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    new_dock = "INSERT INTO docks" \
               " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9)" \
               " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8, p9)
    mycursor.execute(new_dock)
    mydb.commit()
    return 0


def get_dock(num):
    query = "SELECT * FROM docks WHERE num = {}".format(num)
    mycursor.execute(query)
    dock_values = mycursor.fetchone()
    mydb.commit()
    return dock_values


create_table("orders")
create_table("dailyplan")
create_table("facilities")
create_table("docks")

""""
# Testing add_order function
add_order(1, 'Client AA', 18, 'P9', 8, 7, 10, 5, '{1,2,3,4}', 'In Progress')

# Testing add_daily_plan function
add_daily_plan('2022-01-03', 'orders_9, orders_10', 'orders_11, orders_12', 75, 100)

# Testing add_facility function
add_facility(3, 50, 100, 150, 200, 250, 300, 350, 400, 450, 100)

# Testing add_dock function
add_dock(3, 5, 10, 15, 20, 25, 30, 35, 40, 45)

get_id_order, get_client, get_ordernumber, get_workpiece, get_quantity, get_duedate, get_late_penalty, get_early_penalty, get_path, get_status = get_order(1)
print(get_status)
get_date, get_purchase_orders, get_delivery_orders, get_p1_tobuy, get_p2_tobuy = get_daily_plan('2022-01-03')
print(get_date)
get_num_fac, get_p1_fac, get_p2_fac, get_p3_fac, get_p4_fac, get_p5_fac, get_p6_fac, get_p7_fac, get_p8_fac, get_p9_fac, get_worktime_fac = get_facility(3)
print(get_p9_fac)
get_num_dock, get_p1_dock, get_p2_dock, get_p3_dock, get_p4_dock, get_p5_dock, get_p6_dock, get_p7_dock, get_p8_dock, get_p9_dock = get_dock(3)
print(get_p5_dock)
"""
