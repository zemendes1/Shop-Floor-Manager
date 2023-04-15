import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminadmin",
    database="test"
)

mycursor = mydb.cursor()

"""""
mycursor.execute("SHOW TABLES")

mycursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(250),age INTEGER(10))")
sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
student1 = [("Raquel", 12),
            ("Viriato", 11),
            ("Gaspar", 23),
            ("Vento", 55),
            ("João", 25)
            ]
            
mycursor.executemany(sqlFormula, student1)
"""


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


create_table("orders")
create_table("dailyPlan")
create_table("facilitys")
create_table("docks")

mydb.commit()
