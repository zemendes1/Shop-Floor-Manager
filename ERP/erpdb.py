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
student1 = [("Raquel", 12),
            ("Viriato", 11),
            ("Gaspar", 23),
            ("Vento", 55),
            ("João", 25)
            ]

mycursor.executemany(sqlFormula, student1)
mydb.commit()
