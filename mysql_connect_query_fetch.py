import mysql.connector
db_connection = connection = mysql.connector.connect(host='192.168.1.8',
                                         database='user_info',
                                         user='raspberrypi.domain.name',
                                         password='',
                                        )
my_database = db_connection.cursor()
sql_statement = "SELECT id FROM info ORDER BY id DESC LIMIT 1;"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  Id=int(x[0])
  print (Id)

sql_statement_name ="SELECT name FROM info WHERE id=%d;"%Id
my_database.execute(sql_statement_name)
output2 = my_database.fetchall()
for y in output2:
    name=y[0]
    print(name)