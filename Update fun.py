import mysql.connector as m
mydatabase = m.connect(host="localhost",user="root",password="mahendra",database="project")

#function to Check employee id is exist or not
def check_emp(emp_id):
    sql = 'SELECT * FROM Employee_Table WHERE emp_id=%s'
    c = mydatabase.cursor(buffered=True)
    data = (emp_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def update_emp():
    emp_id = input("Enter Employee Id: ")
    if not check_emp(emp_id):
        print("Employee does not exist\n")
    else:
        Name = input("Enter Employee Name: ")
        Mob_Number = input("Enter Employee Mobile Number: ")
        Email = input("Enter Employee Email: ")
        Branch = input("Enter Employee Branch Name: ")
        Date_of_joining = input("Enter Employee Date of joining (YYYY-MM-DD): ")
        
# Only update the fields that are provided (not empty)
        update_fields = []
        if Name:
            update_fields.append("Name=%s")
        if Mob_Number:
            update_fields.append("Mob_Number=%s")
        if Email:
            update_fields.append("Email=%s")
        if Branch:
            update_fields.append("Branch=%s")
        if Date_of_joining:
            update_fields.append("Date_of_joining=%s")
        
        # using query based on provided fields
        update_query = 'UPDATE Employee_Table SET ' + ', '.join(update_fields) + ' WHERE emp_id=%s'
        update_data = []
        if Name:
            update_data.append(Name)
        if Mob_Number:
            update_data.append(Mob_Number)
        if Email:
            update_data.append(Email)
        if Branch:
            update_data.append(Branch)
        if Date_of_joining:
            update_data.append(Date_of_joining)
        update_data.append(emp_id)

        # Execute the update query
        c = mydatabase.cursor()
        c.execute(update_query, tuple(update_data))
        mydatabase.commit()
        print("Employee details updated successfully")

update_emp()
