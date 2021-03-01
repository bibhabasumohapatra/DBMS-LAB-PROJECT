import mysql.connector  

con = mysql.connector.connect(host = 'localhost',user = 'bm',password = 'gulu1610',database = 'motor_parts_shop' )

print(con)