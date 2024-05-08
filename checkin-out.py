import mysql.connector
from datetime import datetime,time

# Connect to the database
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='JATT123 sengh',
                             database='employee')

c=connection.cursor(buffered=True)


def check_in(emp_id):
    try:
        
        check_in_time = datetime.now().time()
        today=datetime.now()
        date = today.day
        month = today.month
        year = today.year
        hour = today.hour
        minute = today.minute
        print()
        print("Your checkin time is {} : {} ".format(hour,minute))
        
        #c.execute('''SELECT emp_id FROM hr WHERE emp_id = %s''', (emp_id,))
        #existing_record = c.fetchone()
        
        c.execute('''SELECT emp_id FROM hr WHERE emp_id = %s AND date = %s AND month = %s AND year = %s''', (emp_id, date, month, year))
        existing_entry = c.fetchone()

        if existing_entry:
            print("You have already checked in for today.")
            return None
            
        else:
            # If no record exists for today, insert a new record
            c.execute('''INSERT INTO hr (emp_id, date, month, year)
                         VALUES (%s, %s, %s, %s)''', (emp_id,date, month, year))
            connection.commit()
        
        print("Check-in successful!")
        return check_in_time
      
    except Exception as e:
        print("Error: check in not done", e)
      
        
        
def check_out(emp_id,check_in_time):
    try:
        
        now = datetime.now().time()
        today=datetime.now()
        date = today.day
        month = today.month
        year = today.year
        # Calculate total working hours
        total_hours = (datetime.combine(datetime.today(), now) - datetime.combine(datetime.today(),check_in_time)).total_seconds() / 3600
        
        c.execute('''SELECT full_day, half_day, total_leaves FROM hr WHERE emp_id = %s''', (emp_id,))
        result = c.fetchone()
        if result:
             full_day, half_day, total_leaves = result

             if total_hours < 5:
            
                     half_day += 1
             else:
                     full_day += 1       
                
                # Calculate total attendance
             total_attendance = full_day + (half_day / 2) - total_leaves
                
                # Update the record in the database
             c.execute('''UPDATE hr SET full_day = %s, half_day = %s, total_leaves = %s, total_attendance = %s 
                         WHERE emp_id = %s AND date = %s AND month = %s AND year = %s''', 
                      (full_day, half_day, total_leaves, total_attendance, emp_id, date, month, year))
        
            

        
        print("Total working hours today is {}".format(total_hours))
  
        connection.commit()

        connection.close()
        print()
        print("Check-out successful!")
    except Exception as e:
        print("Error: check-out not successfull", e)
        return None
        
def main():
    emp_id=int(input("Please enter employee id"))
    
    while True:
        print("\n1.Check In\n2.Check Out\n3.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            check_in_time=check_in(emp_id)
            
        elif choice == '2':
            check_out(emp_id,check_in_time)
        elif choice=="3":
            break
        
        else:
            print("invalid choice")    
        
if __name__=="__main__":
    main()


               
        