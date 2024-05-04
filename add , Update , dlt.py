import mysql.connector as m

mydatabase = m.connect(host="localhost", user="root", password="Dhruv@2981", database="dhruv")

def check_emp(employee_id):
    sql = 'SELECT * FROM employee_table WHERE emp_id=%s'
    c = mydatabase.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def add_emp():
    emp_id = input("Enter Employee Id: ")
    if check_emp(emp_id):
        print("Employee already exists\n")
    else:
        Name = input("Enter Employee Name: ")
        Mob_Number = input("Enter Employee Mobile Number: ")
        Email = input("Enter Employee Email: ")
        Branch = input("Enter Employee Branch Name: ")
        Date_of_joining = input("Enter Employee Date of joining: ")
        data = (emp_id, Name, Mob_Number, Email, Branch, Date_of_joining)
        sql = 'INSERT INTO employee_table (emp_id, Name, Mob_Number, Email, Branch, Date_of_joining) VALUES (%s, %s, %s, %s, %s, %s)'
        c = mydatabase.cursor()
        c.execute(sql, data)
        mydatabase.commit()
        print("Employee Added Successfully")

def update_emp():
    emp_id = input("Enter Employee Id: ")
    if not check_emp(emp_id):
        print("Employee does not exist\n")
    else:
        fields = ["Name", "Mob_Number", "Email", "Branch", "Date_of_joining"]
        print("Choose the field to update:")
        for i, field in enumerate(fields, start=1):
            print(f"{i}. {field}")
        choice = int(input("Enter your choice: "))
        field_to_update = fields[choice - 1]
        new_value = input(f"Enter new value for {field_to_update}: ")
        sql = f'UPDATE employee_table SET {field_to_update} = %s WHERE emp_id = %s'
        data = (new_value, emp_id)
        c = mydatabase.cursor()
        c.execute(sql, data)
        mydatabase.commit()
        print("Employee Updated Successfully")

def delete_emp():
    emp_id = input("Enter Employee Id: ")
    if not check_emp(emp_id):
        print("Employee does not exist\n")
    else:
        sql_select = 'SELECT * FROM employee_table WHERE emp_id=%s'
        c_select = mydatabase.cursor(buffered=True)
        c_select.execute(sql_select, (emp_id,))
        deleted_employee_data = c_select.fetchone()

        
        sql_delete = 'DELETE FROM employee_table WHERE emp_id=%s'
        c_delete = mydatabase.cursor()
        c_delete.execute(sql_delete, (emp_id,))
        mydatabase.commit()
        print("Employee Deleted Successfully")

        
        sql_insert = 'INSERT INTO deleted_empt (emp_id, Name, Mob_Number, Email, Branch, Date_of_joining) VALUES (%s, %s, %s, %s, %s, %s)'
        c_insert = mydatabase.cursor()
        c_insert.execute(sql_insert, deleted_employee_data)
        mydatabase.commit()
        print("Employee data inserted into deleted_empt table")

def main():
    while True:
        print("\n1. Add Employee\n2. Update Employee\n3. Delete Employee\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_emp()
        elif choice == '2':
            update_emp()
        elif choice == '3':
            delete_emp()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

