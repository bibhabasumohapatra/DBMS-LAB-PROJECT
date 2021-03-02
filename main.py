#importing libraries
import mysql.connector  




#main class of db
class motor_parts_DB:

    def __init__(self):
        
        self.con = mysql.connector.connect(host = 'localhost',user = 'bm',password = 'gulu1610',database = 'motor_parts_shop' )
        
        #create a table if not created .......do it after all this ......now not required
    def create_tables(self):
        pass    

    

    #def_insert inserts data into databases 
    def insert_cust_detail(self,cust_name ,car,part_damaged,date_entry ,date_comp ,payment):
        query = "insert into cust_detail(cust_name ,car,part_damaged,date_entry ,date_comp ,payment) values('{}','{}','{}','{}','{}',{})".format(cust_name ,car,
                                                                                                                                                 part_damaged,date_entry,
                                                                                                                                                 date_comp ,payment)


        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted data to customer db")

    def insert_stock_spare_parts(self,parts_name,parts_available,parts_required ,price):

        query = "insert into stock_spare_parts(parts_name,parts_available,parts_required ,price) values('{}',{},{},{})".format(parts_name,parts_available,
                                                                                                                               parts_required ,price)                                                                                     

        
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted data to stock spare parts--- db")


    def insert_emp_details(self,emp_name,emp_mobile,emp_address,emp_department,current_salary):

        query = "insert into emp_details(emp_name,emp_mobile,emp_address,emp_department,current_salary) values('{}',{},'{}','{}',{})".format(emp_name,emp_mobile,
                                                                                                                                                   emp_address,emp_department,
                                                                                                                                                   current_salary)                                                                                     

        
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted data to emp_details--- db")

    def delete_cust_detail(self,token_id):
        
        query = "delete from cust_detail where token_id={}".format(token_id)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted" + " " + str(token_id))

    def delete_stock_spare_parts(self,id):
        
        query = "delete from stock_spare_parts where id={}".format(id)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted" + " " + str(id))

    def delete_emp_details(self,emp_id):
        
        query = "delete from emp_details where emp_id={}".format(emp_id)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted" + " " + str(emp_id))

    


#declaring definations
motor_db = motor_parts_DB()

#make sure testing is 0 after you do your work
testing = 0
if testing == 1:
    #motor_db.insert_cust_detail("bibhabasu","tesla","tyres","2nd feb","22nd feb",22000)
    motor_db.insert_stock_spare_parts("tyres",5,6,2000)
    motor_db.delete_cust_detail(1)
