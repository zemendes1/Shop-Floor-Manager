import psycopg2
import datetime
import math


def connect_to_database():
    global mydb
    try:
        mydb
    except NameError:
        mydb = None

    mydb = psycopg2.connect(
        host="db.fe.up.pt",
        user="up201906869",
        password="infi2023",
        database="up201906869"
    )


def create_table(_table):
    connect_to_database()
    mycursor = mydb.cursor()
    # CREATE TABLE
    create_script = ""
    if _table == "orders":
        create_script = " CREATE TABLE IF NOT EXISTS orders (" \
                        "id INT PRIMARY KEY," \
                        "Client varchar(200) NOT NULL," \
                        "OrderNumber INT," \
                        "WorkPiece varchar(200) NOT NULL," \
                        "Quantity INT," \
                        "DueDate INT," \
                        "Late_Penalty INT," \
                        "Early_Penalty INT," \
                        "path varchar(200)," \
                        "status varchar(200) CHECK (status = 'TBD' OR status='DONE' OR status='IN_PROGRESS')NOT NULL," \
                        "custo INT " \
                        ");"
    elif _table == "order_status":
        create_script = " CREATE TABLE IF NOT EXISTS order_status(" \
                        "id INT PRIMARY KEY," \
                        "OrderNumber INT," \
                        "done_pieces varchar(200) NOT NULL," \
                        "pending_pieces varchar(200) NOT NULL," \
                        "total INT not null," \
                        "total_production_time TIME not null" \
                        ");"
    elif _table == "dailyplan":
        create_script = "CREATE TABLE IF NOT EXISTS dailyPlan (" \
                        "date INT CHECK (date >=0)," \
                        "Working_orders varchar(300)," \
                        "Delivery_orders varchar(300), " \
                        "P1_toBuy INT CHECK (P1_toBuy >= 0)," \
                        "P2_toBuy INT CHECK (P2_toBuy >= 0)," \
                        "P1_Arriving INT CHECK (P1_Arriving>=0)," \
                        "P2_Arriving INT CHECK (P2_Arriving>=0)" \
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
    elif _table == "day":
        create_script = "CREATE TABLE IF NOT EXISTS day (" \
                        "day INT not null," \
                        "time_elapsed TIME NOT NULL " \
                        ");"
    elif _table == "warehouse":
        create_script = "CREATE TABLE IF NOT EXISTS warehouse (" \
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
        create_script = "CREATE OR REPLACE VIEW docks_total AS SELECT " \
                        "num,P1,P2,P3,P4,P5,P6,P7,P8,P9,(P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9) AS Total " \
                        "FROM docks;"

    elif _table == "current_order_list":
        create_script = "CREATE OR REPLACE VIEW in_progress_view AS SELECT id, client, ordernumber, workpiece," \
                        " quantity, duedate, late_penalty, early_penalty, path, status " \
                        "FROM orders WHERE status = 'IN_PROGRESS';"

    mycursor.execute(create_script)
    mydb.commit()


def add_order(id_order, client, ordernumber, workpiece, quantity, duedate,
              late_penalty, early_penalty, path, status, custo):
    connect_to_database()
    mycursor = mydb.cursor()

    # Check if entry with given id_order already exists
    mycursor.execute("SELECT * FROM orders WHERE id = %s", (id_order,))
    existing_entry = mycursor.fetchone()

    # If entry exists, do not add new order and return -1
    if existing_entry:
        return 1

    # If entry does not exist, add new order to database
    new_order = "INSERT INTO orders" \
                " (id, client, ordernumber, workpiece, quantity, duedate," \
                " late_penalty, early_penalty, path, status, custo)" \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty,
              path, status, custo)
    mycursor.execute(new_order, values)
    mydb.commit()
    return 0


def update_order(id_order, client, ordernumber, workpiece, quantity, duedate, late_penalty, early_penalty, path,
                 status, custo):
    connect_to_database()
    mycursor = mydb.cursor()

    new_order = "UPDATE orders SET " \
                "client='{}', ordernumber={}, workpiece='{}', quantity={}, duedate={}, late_penalty={}," \
                " early_penalty={}, path='{}', status='{}', custo={}" \
                " WHERE id={}".format(client, ordernumber, workpiece, quantity, duedate, late_penalty,
                                      early_penalty, path, status, id_order, custo)
    mycursor.execute(new_order)
    mydb.commit()
    return 0


def get_order(id_order):
    connect_to_database()
    mycursor = mydb.cursor()

    if id_order is None:
        query = "SELECT * FROM orders order by DueDate"
        mycursor.execute(query)
        order_values = mycursor.fetchall()
        mydb.commit()
    else:
        query = "SELECT * FROM orders WHERE id= {}".format(id_order)
        mycursor.execute(query)
        order_values = mycursor.fetchone()
        mydb.commit()
    return order_values


def get_order_status(status_of_order):
    connect_to_database()
    mycursor = mydb.cursor()

    if status_of_order in ('TBD', 'DONE', 'IN_PROGRESS'):
        query = "SELECT * FROM orders WHERE status = %s ORDER BY id DESC"
        mycursor.execute(query, (status_of_order,))
        order_values = mycursor.fetchall()
        mydb.commit()
        return order_values
    else:
        return 'ERROR'


def update_order_status(order, new_status):
    connect_to_database()
    mycursor = mydb.cursor()

    query = "UPDATE orders SET status = '{}' WHERE id = '{}';".format(new_status, order)
    mycursor.execute(query)
    mydb.commit()
    return 0


def add_daily_plan(date, working_orders, delivery_orders, p1_tobuy, p2_tobuy, p1_Arriving, p2_Arriving):
    connect_to_database()
    mycursor = mydb.cursor()

    # Check if entry with given date already exists
    mycursor.execute("SELECT * FROM dailyplan WHERE date = %s", (date,))
    existing_entry = mycursor.fetchone()

    # If entry exists, do not add new plan and return -1
    if existing_entry:
        return 1

    else:
        # If entry does not exist, add new plan to database
        new_plan = "INSERT INTO dailyplan" \
                   " (date, working_orders, delivery_orders, p1_tobuy, p2_tobuy, p1_Arriving, p2_Arriving)" \
                   " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (date, working_orders, delivery_orders, p1_tobuy, p2_tobuy, p1_Arriving, p2_Arriving)
        mycursor.execute(new_plan, values)
        mydb.commit()
    return 0


def get_daily_plan(date):
    connect_to_database()
    mycursor = mydb.cursor()

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


def update_daily_plan(date, working_orders, delivery_orders, p1_tobuy, p2_tobuy, p1_Arriving, p2_Arriving):
    connect_to_database()
    mycursor = mydb.cursor()

    update_plan = "UPDATE dailyplan SET working_orders = '{}', delivery_orders = '{}'" \
                  ", p1_tobuy = {}, p2_tobuy = {}" \
                  " WHERE date = '{}';".format(working_orders, delivery_orders, p1_tobuy,
                                               p2_tobuy, p1_Arriving, p2_Arriving, date)
    mycursor.execute(update_plan)
    mydb.commit()
    return 0


def add_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    connect_to_database()
    mycursor = mydb.cursor()

    # Check if the entry exists
    check_query = "SELECT EXISTS(SELECT 1 FROM facilities WHERE num = {} )".format(num)
    mycursor.execute(check_query)
    result = mycursor.fetchone()[0]

    if result:
        # The entry exists, so don't insert it again
        return 1
    else:
        # The entry doesn't exist, so insert it
        time = convert_ms_to_postgre_time(work_time)
        new_facility = "INSERT INTO facilities" \
                       " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9, worktime)" \
                       " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}');".format(num, p1, p2, p3, p4, p5, p6,
                                                                                        p7,
                                                                                        p8, p9, time)
        mycursor.execute(new_facility)
        mydb.commit()

    return 0


def update_facility(num, p1, p2, p3, p4, p5, p6, p7, p8, p9, work_time):
    connect_to_database()
    mycursor = mydb.cursor()

    time = convert_ms_to_postgre_time(work_time)
    update_query = "UPDATE facilities SET p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={}," \
                   "worktime='{}' WHERE num={}".format(p1, p2, p3, p4, p5, p6, p7, p8, p9, time, num)
    mycursor.execute(update_query)
    mydb.commit()
    return 0


def get_facility(num):
    connect_to_database()
    mycursor = mydb.cursor()

    if num is None:
        query = "SELECT * FROM facilities order by num "
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
    connect_to_database()
    mycursor = mydb.cursor()

    # Check if the entry exists
    check_query = "SELECT EXISTS(SELECT 1 FROM docks WHERE num = {})".format(num)
    mycursor.execute(check_query)
    result = mycursor.fetchone()[0]

    if result:
        # The entry exists, so don't insert it again
        return 1

    else:
        # The entry doesn't exist, so insert it
        new_dock = "INSERT INTO docks" \
                   " (num, p1, p2, p3, p4, p5, p6, p7, p8, p9)" \
                   " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(num, p1, p2, p3, p4, p5, p6, p7, p8,
                                                                              p9)
        mycursor.execute(new_dock)
        mydb.commit()

    return 0


def update_dock(num, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    connect_to_database()
    mycursor = mydb.cursor()

    update_query = "UPDATE docks SET p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={} " \
                   "WHERE num={}".format(p1, p2, p3, p4, p5, p6, p7, p8, p9, num)
    mycursor.execute(update_query)
    mydb.commit()
    return 0


def get_dock(num):
    connect_to_database()
    mycursor = mydb.cursor()

    if num is None:
        query = "SELECT * FROM docks order by num"
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
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM docks; DELETE FROM facilities; DELETE FROM orders; DELETE FROM dailyplan;" \
            "DELETE FROM order_status; DELETE FROM day; DELETE FROM warehouse;"
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


def insert_or_update_time(elapsed_time):
    connect_to_database()
    mycursor = mydb.cursor()

    # check if row already exists for this day
    try:
        mycursor.execute("SELECT * FROM day")
        existing_row = mycursor.fetchone()
        # Define the number of milliseconds in a day
        MILLISECONDS_PER_DAY = 60 * 1000
        # Calculate the number of days
        current_day = math.ceil(elapsed_time / MILLISECONDS_PER_DAY) - 1

        if existing_row:
            # update existing row with new day and time_elapsed values
            mycursor.execute(
                "UPDATE day SET day={}, time_elapsed='{}'".format(current_day,
                                                                  convert_ms_to_postgre_time(elapsed_time)))
            mydb.commit()
        else:
            try:
                # insert new row with day and time_elapsed values
                mycursor.execute("INSERT INTO day (day, time_elapsed) VALUES"
                                 " ({}, '{}')".format(current_day, convert_ms_to_postgre_time(elapsed_time)))
                mydb.commit()
                # code that interacts with the database
            except psycopg2.Error as e:
                print("An error occurred:", str(e))

    # code that interacts with the database
    except psycopg2.Error as e:
        print("An error occurred:", str(e))


def get_day():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "SELECT day FROM day"
    mycursor.execute(query)
    dia = mycursor.fetchall()
    if dia is not None:
        return dia[0][0]
    else:
        return 0


def add_warehouse(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    connect_to_database()
    mycursor = mydb.cursor()
    new_warehouse = "INSERT INTO warehouse" \
                    " (p1, p2, p3, p4, p5, p6, p7, p8, p9)" \
                    " VALUES ( {}, {}, {}, {}, {}, {}, {}, {}, {});".format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    mycursor.execute(new_warehouse)
    mydb.commit()
    return 0


def update_warehouse(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    connect_to_database()
    mycursor = mydb.cursor()

    update_query = "UPDATE warehouse SET" \
                   " p1={}, p2={}, p3={}, p4={}, p5={}, p6={}, p7={}, p8={}, p9={}".format(p1, p2, p3, p4, p5,
                                                                                           p6, p7, p8, p9)
    mycursor.execute(update_query)
    mydb.commit()
    return 0


def get_warehouse(text):
    connect_to_database()
    mycursor = mydb.cursor()

    if text is None:
        query = "SELECT * FROM warehouse"
        mycursor.execute(query)
        warehouse_values = mycursor.fetchall()
        mydb.commit()
        return warehouse_values[0]
    else:
        query = "SELECT {} FROM warehouse ".format(str(text))
        mycursor.execute(query)
        warehouse_values = mycursor.fetchone()
        mydb.commit()
        return warehouse_values[0]


def erase_docks():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM docks;"
    mycursor.execute(query)
    mydb.commit()


def erase_orders():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM orders;"
    mycursor.execute(query)
    mydb.commit()


def erase_dailyplan():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM dailyplan;"
    mycursor.execute(query)
    mydb.commit()


def erase_facilities():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM facilities;"
    mycursor.execute(query)
    mydb.commit()


def erase_order_status():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM order_status;"
    mycursor.execute(query)
    mydb.commit()


def erase_warehouse():
    connect_to_database()
    mycursor = mydb.cursor()

    query = "DELETE FROM warehouse;"
    mycursor.execute(query)
    mydb.commit()


def remove_piece_from_warehouse(piece_type, number_of_pieces):
    connect_to_database()
    mycursor = mydb.cursor()

    if piece_type is not None:
        query = "SELECT * FROM warehouse"
        mycursor.execute(query)
        warehouse_values = mycursor.fetchall()
        mydb.commit()
        p1, p2, p3, p4, p5, p6, p7, p8, p9 = warehouse_values[0]

        update_query = "DELETE FROM warehouse"
        mycursor.execute(update_query)
        mydb.commit()

        if "p" + piece_type[1] == "p1":
            add_warehouse(p1 - number_of_pieces, p2, p3, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p2":
            add_warehouse(p1, p2 - number_of_pieces, p3, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p3":
            add_warehouse(p1, p2, p3 - number_of_pieces, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p4":
            add_warehouse(p1, p2, p3, p4 - number_of_pieces, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p5":
            add_warehouse(p1, p2, p3, p4, p5 - number_of_pieces, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p6":
            add_warehouse(p1, p2, p3, p4, p5, p6 - number_of_pieces, p7, p8, p9)
        elif "p" + piece_type[1] == "p7":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7 - number_of_pieces, p8, p9)
        elif "p" + piece_type[1] == "p8":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7, p8 - number_of_pieces, p9)
        elif "p" + piece_type[1] == "p9":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7, p8, p9 - number_of_pieces)


def add_piece_to_warehouse(piece_type, number_of_pieces):
    connect_to_database()
    mycursor = mydb.cursor()

    if piece_type is not None:
        query = "SELECT * FROM warehouse"
        mycursor.execute(query)
        warehouse_values = mycursor.fetchall()
        mydb.commit()
        p1, p2, p3, p4, p5, p6, p7, p8, p9 = warehouse_values[0]

        update_query = "DELETE FROM warehouse"
        mycursor.execute(update_query)
        mydb.commit()

        if "p" + piece_type[1] == "p1":
            add_warehouse(p1 + number_of_pieces, p2, p3, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p2":
            add_warehouse(p1, p2 + number_of_pieces, p3, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p3":
            add_warehouse(p1, p2, p3 + number_of_pieces, p4, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p4":
            add_warehouse(p1, p2, p3, p4 + number_of_pieces, p5, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p5":
            add_warehouse(p1, p2, p3, p4, p5 + number_of_pieces, p6, p7, p8, p9)
        elif "p" + piece_type[1] == "p6":
            add_warehouse(p1, p2, p3, p4, p5, p6 + number_of_pieces, p7, p8, p9)
        elif "p" + piece_type[1] == "p7":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7 + number_of_pieces, p8, p9)
        elif "p" + piece_type[1] == "p8":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7, p8 + number_of_pieces, p9)
        elif "p" + piece_type[1] == "p9":
            add_warehouse(p1, p2, p3, p4, p5, p6, p7, p8, p9 + number_of_pieces)


def number_of_orders_stored():
    connect_to_database()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT count(id) FROM orders ")
    number_of_orders = mycursor.fetchone()
    mydb.commit()
    return number_of_orders[0]


def db_startup():
    create_table("orders")
    create_table("dailyplan")
    create_table("facilities")
    create_table("docks")
    create_table("day")
    create_table("warehouse")

    erase_orders()

    erase_dailyplan()

    erase_docks()
    add_dock(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_dock(2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    erase_facilities()
    add_facility(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    add_facility(4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    erase_warehouse()
    add_warehouse(0, 0, 0, 0, 0, 0, 0, 0, 0)
    erase_order_status()
