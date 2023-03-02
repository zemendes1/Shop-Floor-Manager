import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminadmin",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(250),age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
student1 = [("Rachel", 27),
            ("Vítor", 20),
            ("Gavínio", 25),
            ("Vimieiro", 24),
            ("Jacaré", 21)
            ]

mycursor.executemany(sqlFormula, student1)
mydb.commit()
