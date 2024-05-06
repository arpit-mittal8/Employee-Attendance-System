import mysql.connector
from datetime import datetime,time

# Connect to the database
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='JATT123 sengh',
                             database='employee')

c=connection.cursor()


def check_in(emp_id):
    try:
        
        check_in_time = datetime.now().time()
        today=datetime.now()
        date = today.day
        month = today.month
        year = today.year
        
        #c.execute('''INSERT INTO Empt (emp_id, check_in_date, check_in_month, check_in_year)
        #              VALUES (%s, %s, %s, %s)''', (emp_id, date, month, year))
        #connection.commit()
        
        print("Check-in successful!")
        return check_in_time
      
    except Exception as e:
        print("Error: check in not done", e)
      
        
        
def check_out(emp_id,check_in_time):
    try:
        
        now = datetime.now().time()
        # Calculate total working hours
        total_hours = (datetime.combine(datetime.today(), now) - datetime.combine(datetime.today(),check_in_time)).total_seconds() / 3600
        if total_hours < 5:
            c.execute('''UPDATE hrempt SET half_day = half_day + 1 WHERE emp_id = %s''', (emp_id,))
        else:
            c.execute('''UPDATE hrempt SET full_day = full_day + 1 WHERE emp_id = %s''', (emp_id,))
        
        c.execute('''UPDATE hrempt SET total_attendance = (full_day + (half_day / 2) - total_leaves)''')
  
        connection.commit()
        connection.close()
        print("Check-out successful!")
    except Exception as e:
        print("Error: check-out not successfull", e)
        
def main():
    emp_id=int(input("Please enter employee id"))
    while True:
        print("\n1.Check In\n2.Check Out")
        choice = input("Enter your choice: ")
        if choice == '1':
            check_in_time=check_in(emp_id)
            
        elif choice == '2':
            check_out(emp_id,check_in_time)
            break
        
        else:
            print("invalid choice")    
        
if __name__=="__main__":
    main()


               
        