#importing libraries
import mysql.connector  




#main class of db
class motor_parts_DB:

    def __init__(self):
        
        self.con = mysql.connector.connect(host = 'localhost',user = 'bm',password = 'gulu1610',database = 'motor_parts_shop' )

    

    #def_insert inserts data into databases 
    def insert_cust_detail(self,cust_name ,car,part_damaged,date_entry ,date_comp ,payment):
        query = "insert into cust_detail(cust_name ,car,part_damaged,date_entry ,date_comp ,payment) values('{}','{}','{}','{}','{}',{})".format(cust_name ,car,
                                                                                                                                                 part_damaged,date_entry,
                                                                                                                                                 date_comp ,payment)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted data to db")








#declaring definations
motor_db = motor_parts_DB()
#motor_db.insert_cust_detail("bibhabasu","tesla","tyres","2nd feb","22nd feb",22000)
