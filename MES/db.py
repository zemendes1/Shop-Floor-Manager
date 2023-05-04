import psycopg2
import datetime

mydb = psycopg2.connect(
    host="db.fe.up.pt",
    user="up201906869",
    password="infi2023",
    database="up201906869"
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

    elif _table == "dailyplan":
        create_script = "CREATE TABLE IF NOT EXISTS dailyPlan (" \
                        "date INT CHECK (date >=0)," \
                        "Purchase_orders varchar(40)," \
                        "Delivery_orders varchar(100), " \
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
                        "workTime TIME NOT NULL" \
                        ");"
    elif _table == "facilities_total":
        create_script = "CREATE VIEW facilities_total AS SELECT " \
                        "num,P1,P2,P3,P4,P5,P6,P7,P8,P9,workTime,(P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9) " \
                        "AS Total " \
                        "FROM facilities;"
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
    elif _table == "docks_total":
        create_script = "CREATE VIEW docks_total AS SELECT " \
                        "num,P1,P2,P3,P4,P5,P6,P7,P8,P9,(P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9) AS Total " \
                        "FROM docks;"
    mycursor.execute(create_script)
    mydb.commit()


def add_order(id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status):
    # Check if entry with given id_order already exists
    mycursor.execute("SELECT * FROM orders WHERE id = %s", (id_order,))
    existing_entry = mycursor.fetchone()

    # If entry exists, do not add new order and return -1
    if existing_entry:
        # print("Entry already exists for facility number {}".format(id_order))
        return 1

    # If entry does not exist, add new order to database
    new_order = "INSERT INTO orders" \
                " (id, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status)" \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status)
    mycursor.execute(new_order, values)
    mydb.commit()
    # print("New entry added for facility number {}".format(id_order))
    return 0


# update_query = "UPDATE facilities SET p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={}," \
#                  "worktime='{}' WHERE num={}".format(p1, p2, p3, p4, p5, p6, p7, p8, p9, time, num)

def update_order(id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path,
                 status):
    new_order = "UPDATE orders SET " \
                "client='{}', ordernumber={}, workpiece='{}', quantity={}, duedate={}, late_penalty={}," \
                " early_penalty={}, path='{}', status='{}'" \
                " WHERE id={}".format(client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty,
                                      path, status, id_order)
    mycursor.execute(new_order)
    mydb.commit()
    return 0


def get_order(id_order):
    if id_order is None:
        query = "SELECT * FROM orders ORDER BY id DESC"
        mycursor.execute(query)
        order_values = mycursor.fetchall()
        mydb.commit()
    else:
        query = "SELECT * FROM orders WHERE id= {}".format(id_order)
        mycursor.execute(query)
        order_values = mycursor.fetchone()
        mydb.commit()
    return order_values


def add_daily_plan(date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy):
    # Check if entry with given date already exists
    mycursor.execute("SELECT * FROM dailyplan WHERE date = %s", (date,))
    existing_entry = mycursor.fetchone()

    # If entry exists, do not add new plan and return -1
    if existing_entry:
        # print("Entry already exists for facility number {}".format(date))
        return 1

    else:
        # If entry does not exist, add new plan to database
        new_plan = "INSERT INTO dailyplan" \
                   " (date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy)" \
                   " VALUES (%s, %s, %s, %s, %s)"
        values = (date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy)
        mycursor.execute(new_plan, values)
        mydb.commit()
        # print("New entry added for facility number {}".format(date))
    return 0


def get_daily_plan(date):
    if date is None:
        query = "SELECT * FROM dailyplan ORDER BY date DESC"
        mycursor.execute(query)
        daily_plan_values = mycursor.fetchall()
        mydb.commit()
    else:
        query = "SELECT * FROM dailyplan WHERE date = '{}'".format(date)
        mycursor.execute(query)
        daily_plan_values = mycursor.fetchone()
        mydb.commit()
    return daily_plan_values


def update_daily_plan(date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy):
    update_plan = "UPDATE dailyplan SET purchase_orders = '{}', delivery_orders = '{}', p1_tobuy = {}, p2_tobuy = {}" \
                  " WHERE date = '{}';".format(purchase_orders, delivery_orders, p1_tobuy, p2_tobuy, date)
    mycursor.execute(update_plan)
    mydb.commit()
    return 0


def add_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    # Check if the entry exists
    check_query = "SELECT EXISTS(SELECT 1 FROM facilities WHERE num = {} )".format(num)
    mycursor.execute(check_query)
    result = mycursor.fetchone()[0]

    if result:
        # The entry exists, so don't insert it again
        # print("Entry already exists for facility number {}".format(num))
        return 1
    else:
        # The entry doesn't exist, so insert it
        time = convert_ms_to_postgre_time(work_time)
        new_facility = "INSERT INTO facilities" \
                       " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9, worktime)" \
                       " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}');".format(num, p1, p2, p3, p4, p5, p6, p7,
                                                                                        p8, p9, time)
        mycursor.execute(new_facility)
        mydb.commit()
        # print("New entry added for facility number {}".format(num))

    return 0


def update_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    time = convert_ms_to_postgre_time(work_time)
    update_query = "UPDATE facilities SET p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={}," \
                   "worktime='{}' WHERE num={}".format(p1, p2, p3, p4, p5, p6, p7, p8, p9, time, num)
    mycursor.execute(update_query)
    mydb.commit()
    return 0


def get_facility(num):
    if num is None:
        query = "SELECT * FROM facilities order by num asc"
        mycursor.execute(query)
        facility_values = mycursor.fetchall()
        mydb.commit()

    else:
        query = "SELECT * FROM facilities WHERE num = {}".format(num)
        mycursor.execute(query)
        facility_values = mycursor.fetchone()
        mydb.commit()
    return facility_values


def add_dock(num, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    # Check if the entry exists
    check_query = "SELECT EXISTS(SELECT 1 FROM docks WHERE num = {})".format(num)
    mycursor.execute(check_query)
    result = mycursor.fetchone()[0]

    if result:
        # The entry exists, so don't insert it again
        # print("Entry already exists for dock number {}".format(num))
        return 1

    else:
        # The entry doesn't exist, so insert it
        new_dock = "INSERT INTO docks" \
                   " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9)" \
                   " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8, p9)
        mycursor.execute(new_dock)
        mydb.commit()
        # print("New entry added for dock number {}".format(num))

    return 0


def update_dock(num, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    update_query = "UPDATE docks SET p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={} WHERE num={}".format(
        p1, p2, p3, p4, p5, p6, p7, p8, p9, num)
    mycursor.execute(update_query)
    mydb.commit()
    return 0


def get_dock(num):
    if num is None:
        query = "SELECT * FROM docks order by num asc"
        mycursor.execute(query)
        dock_values = mycursor.fetchall()
        mydb.commit()
    else:
        query = "SELECT * FROM docks WHERE num = {}".format(num)
        mycursor.execute(query)
        dock_values = mycursor.fetchone()
        mydb.commit()
    return dock_values


def reset_db():
    query = "DELETE FROM docks; DELETE FROM facilities; DELETE FROM orders; DELETE FROM dailyplan;"
    mycursor.execute(query)
    mydb.commit()

    add_facility(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    add_dock(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_dock(2, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def convert_ms_to_postgre_time(ms):
    delta = datetime.timedelta(milliseconds=ms)
    microseconds = delta.microseconds
    seconds = delta.seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{microseconds:03d}"


""""
create_table("orders")
create_table("dailyplan")
create_table("facilities")
create_table("docks")
create_table("docks_total")

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

#Test_Updates
update_order(1, 'Client BB', 18, 'P9', 8, 7, 10, 5, '{1,2,3,4}', 'In Progress')
update_daily_plan(7, 'orders_1, orders_2', 'P3_from_P2, P3_from_P2, null, null', 75, 100)
update_facility(4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
update_dock(1, 1, 1, 2, 3, 4, 5, 0, 0, 0)

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

