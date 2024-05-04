from datetime import date
import mysql.connector

# Establishing connection to the MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="project"
)

# Function to check if the employee exists
def check_employee(emp_id):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Empt WHERE emp_id = %s", (emp_id,))
    employee = cursor.fetchone()
    cursor.close()
    return employee is not None

# Function to remove an employee
def remove_employee():
    emp_id = input("Enter Employee ID: ")

    # Checking if the employee exists
    if not check_employee(emp_id):
        print("Employee does not exist.")
        return

    # Query to select employee information before deleting
    select_sql = "select * from Empt where emp_id = %s"
    cursor=con.cursor()
    cursor.execute(select_sql,(emp_id,))
    removed_employee = cursor.fetchone()

    # get the current date
    resign_date= date.today().strftime("%Y-%m-%d")

    # Inserting removed employee into another table

    insert_sql = "insert into Emp_resign (emp_id,Name,Mob_Number,Email,Branch,Date_of_resigning) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_sql, (removed_employee[0], removed_employee[1], removed_employee[2], removed_employee[3], removed_employee[4], resign_date))
    con.commit()
  
    # Deleting employee from the original table

    delete_sql = "delete from Empt where emp_id = %s"
    cursor.execute(delete_sql,(emp_id,))
    con.commit()
    cursor.close()

    print("Employee with ID {} removed successfully".format(emp_id))
  

# Function to display menu
def menu():
    remove_employee()
# Main function
def main():
    menu()
if __name__ == "__main__":
    main()
