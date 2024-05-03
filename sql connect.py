
import mysql.connector as m

mydatabase=m.connect(host="localhost" ,user="root",password="123456",database="project")

cursor=mydatabase.cursor()


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

    # Query to delete employee from the table
    sql = "DELETE FROM Empt WHERE emp_id = %s"
    cursor = con.cursor()
    cursor.execute(sql, (emp_id,))
    con.commit()
    print("Employee removed successfully.")

# Function to display menu
def menu():
    print("\n1. Remove Employee")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        remove_employee()
    elif choice == '2':
        con.close()
        print("Connection closed.")
    else:
        print("Invalid choice.")
# Main function
def main():
    menu()
if __name__ == "__main__":
    main()
