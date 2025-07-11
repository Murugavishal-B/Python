def add_attendance(name, date):
    with open('attendance.txt', 'a') as file:
        file.write(f"{name}, {date}, Present\n")
def view_attendance():
    with open('attendance.txt', 'r') as file:
        records = file.readlines()
        for record in records:
            print(record.strip())
def main():
    while True:
        print("\n1. Add Employee Attendance")
        print("2. View Attendance Records")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter employee name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_attendance(name, date)
            print(f"Attendance recorded for {name} on {date}")
        elif choice == '2':
            print("\nAttendance Records:")
            view_attendance()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
