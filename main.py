#importing libraries
import mysql.connector  
import pandas as pd
from tabulate import tabulate



#main class of db
class motor_parts_DB:

    def __init__(self):
        
        self.con = mysql.connector.connect(host = 'localhost',user = 'bm',password = 'gulu1610',database = 'motor_parts_shop' )
        
        #create a table if not created ......showing some error ......do it later
    def create_tables(self):
        sql_file = "/home/bibhabasu/Desktop/dbms_iiit/db.sql" #assign our file_address
        cur = self.con.cursor()
        for line in open(sql_file):
            cur.execute(line)

        self.con.commit()

        print("created tables")
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


    def insert_emp_details(self,emp_name,emp_address,emp_department,current_salary):

        query = "insert into emp_details(emp_name,emp_address,emp_department,current_salary) values('{}','{}','{}',{})".format(emp_name,
                                                                                                                                emp_address,emp_department,
                                                                                                                                current_salary)                                                                                     

        
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted data to emp_details--- db")

    def delete_cust_detail(self,token_id):
        

        query = "delete from cust_detail where token_id={}".format(token_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted" + " " + str(token_id))


    def delete_stock_spare_parts(self,id):
        

        query = "delete from stock_spare_parts where id={}".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted" + " " + str(id))

    def delete_emp_details(self,emp_id):
        

        query = "delete from emp_details where emp_id={}".format(emp_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted" + " " + str(emp_id))

    def fetch_all(self,table_name):

        cur = self.con.cursor()
        cur.execute('SELECT * FROM {}'.format(table_name))
        table_rows = cur.fetchall()
        if table_name == "cust_detail":

            df = pd.DataFrame(table_rows)
            df.columns = ["cust_id","cust_name" ,"car","part_damaged","date_entry" ,"date_comp" ,"payment"]
        
        if table_name == "stock_spare_parts":
            
            df = pd.DataFrame(table_rows)
            df.columns = ["part_code","parts_name","parts_available","parts_required" ,"price"]


        if table_name == "emp_details":
            
            df = pd.DataFrame(table_rows)
            df.columns = ["emp_id","emp_name","emp_address","emp_department","current_salary"]


        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


    
    
    


#declaring definations
motor_db = motor_parts_DB()

#make sure testing is 0 after you do your work
testing = 1
testing2 = 1
if testing == 1:
    #motor_db.create_tables()
    #motor_db.insert_cust_detail("bibhabasu","tesla","tyres","2nd feb","22nd feb",22000)
    #motor_db.insert_stock_spare_parts("tyres",5,6,2000)
    #motor_db.insert_emp_details("bradd pit","downing street","tyres",6000)


    if testing2  == 1: 
         
        print("\t\t\t\t==================================MENU====================================\n")  
        print("\t\t\t\t1.   INSERT DATA into CUSTOMER TABLE \n")
        print("\t\t\t\t2.   INSERT DATA into STOCK SPARE PARTS \n")
        print("\t\t\t\t3.   INSERT DATA into EMPLOYEE DETAILS \n")
        print("\t\t\t\t4.   DELETE FROM CUSTOMER TABLE\n")
        print("\t\t\t\t5.   DELETE FROM STOCK SPARE PARTS \n")
        print("\t\t\t\t6.   DELETE FROM EMPLOYEE TABLE \n")
        motor_db.fetch_all("cust_detail")
        motor_db.fetch_all("stock_spare_parts")
        motor_db.fetch_all("emp_details")
        
        key = int(input())
        if key == 1:

            print("\nenter cust_name\n")
            cust_name = str(input())
            print("\nenter car model\n")
            car = str(input())
            print("\nenter part damaged\n")
            part = str(input())
            print("\nenter date_entry\n")
            date_entry = str(input())
            print("\nenter date completed\n")
            date_comp = str(input())
            print("\nenter final amount\n")
            price = int(input())
            motor_db.insert_cust_detail(cust_name,car,part,date_entry,date_comp,price)
            print("\ndata entered")


        if key == 2:

            print("part_name")
            part = str(input())
            print("\nenter no. of parts available\n")
            part_available = int(input())
            print("\nenter no. of part required")
            part_required = int(input())
            print("\nprice of each part required\n")
            price = int(input())

            motor_db.insert_stock_spare_parts(part,part_available,part_required,price)

        if key == 3:
            print("Please enter emp_name\n")
            name = str(input())
            print("\nPlease enter address\n")
            address = str(input())
            print("\nPlease enter department\n")
            dept = str(input())
            print("\n Please enter salary\n")
            salary = int(input())

            motor_db.insert_emp_details(name, address,dept,salary)
        if key == 4:
            print("enter cust id")
            cust_id = int(input())
            motor_db.delete_cust_detail(cust_id) 

        if key == 5:
            print("enter part_code id")
            id = int(input())
            motor_db.delete_stock_spare_parts(id)

        if key == 6:
            print("enter employee id")
            id = int(input())
            motor_db.delete_emp_details(id)        

            

                



