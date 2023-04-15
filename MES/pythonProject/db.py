import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12password",
    database="dbteste"
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

    elif _table == "facilitys":
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


def add_order(id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status):
    new_order = "INSERT INTO orders" \
                " (id, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path, status)" \
                " VALUES ({}, '{}', {}, '{}', {}, {}, {}, {}, '{}', '{}');".format(id_order, client, ordernumber,
                                                                                   workpiece,
                                                                                   quantity, duedate, late_penalty,
                                                                                   early_penalty, path, status)

    mycursor.execute(new_order)


def add_daily_plan(date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy):
    new_plan = "INSERT INTO dailyplan" \
               " (date, purchase_orders, delivery_orders, p1_tobuy, p2_tobuy)" \
               " VALUES ('{}', '{}', '{}', {}, {});".format(date, purchase_orders, delivery_orders, p1_tobuy,
                                                            p2_tobuy)
    mycursor.execute(new_plan)


def add_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    new_facility = "INSERT INTO facilities" \
                   " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9, worktime)" \
                   " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8,
                                                                                  p9, work_time)
    mycursor.execute(new_facility)


def add_dock(num, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    new_dock = "INSERT INTO docks" \
               " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9)" \
               " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8, p9)
    mycursor.execute(new_dock)


create_table("orders")
create_table("dailyplan")
create_table("facilitys")
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
"""

mydb.commit()
