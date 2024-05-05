import mysql.connector
from prettytable import PrettyTable


def display_detail():
    def connect_to_database():
        try:
            # Connect to MySQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="company"
            )
            return conn
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
            return None

    def get_access_level(conn, user_id):
        if user_id == 250401:
            return 'HR'
        else:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT access_level FROM Empt WHERE emp_id = %s", (user_id,))
                access_level = cursor.fetchone()
                cursor.close()
                return access_level[0] if access_level else None
            except mysql.connector.Error as err:
                print("Error retrieving access level:", err)
                return None

    def get_all_employee_data(conn):
        try:
            # Query to fetch all data
            query = """
                SELECT e.emp_id, e.Name, e.Mob_Number, e.Email, e.Branch, e.Date_of_joining,
                    a.full_day, a.half_day, a.total_leaves, a.total_attendance
                FROM Empt e
                JOIN hrempt a ON e.emp_id = a.emp_id
            """
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except mysql.connector.Error as err:
            print("Error fetching data for HR:", err)
            return None

    def get_employee_data(conn, emp_id):
        try:
            # Query to fetch data for the specific employee
            query = """
                SELECT e.emp_id, e.Name, e.Mob_Number, e.Email, e.Branch, e.Date_of_joining,
                    a.full_day, a.half_day, a.total_leaves, a.total_attendance
                FROM Empt e
                JOIN hrempt a ON e.emp_id = a.emp_id
                WHERE e.emp_id = %s
            """
            cursor = conn.cursor()
            cursor.execute(query, (emp_id,))
            data = cursor.fetchall()
            cursor.close()
            return data
        except mysql.connector.Error as err:
            print("Error fetching data for employee:", err)
            return None

    def show_table(data):
        if data:
            # Create PrettyTable instance
            table = PrettyTable()
            table.field_names = ["emp_id", "Name", "Mobile No", "Email", "Branch", "Date of Joining",
                                "Full Day", "Half Day", "Total Leaves", "Total Attendance"]

            # Add rows to the table
            for row in data:
                table.add_row(row)

            # Print the table
            print(table)
        else:
            print("No data to display")

    # Example usage
    while True:
        try:
            conn = connect_to_database()
            if conn:
                user_id = int(input("Enter your user id: "))
                access_level = get_access_level(conn, user_id)
                if access_level == 'HR':
                    print("Options:")
                    print("1. See all employee details")
                    print("2. See specific employee detail")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        data = get_all_employee_data(conn)
                        show_table(data)
                    elif choice == '2':
                        emp_id = input("Enter employee ID: ")
                        data = get_employee_data(conn, emp_id)
                        show_table(data)
                    else:
                        print("Invalid choice.")
                else:
                    data = get_employee_data(conn, user_id)
                    show_table(data)
            else:
                print("Failed to establish connection to the database.")
        except ValueError:
            print("Invalid user ID. Please enter a valid numeric user ID.")

if __name__ == "__main__":
    display_detail()