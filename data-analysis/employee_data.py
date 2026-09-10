import csv
import os

FILE_NAME = "employees.csv"

# create file with header if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Serial No", "Name", "Phone No", "ID Card No"])

# read all employee data
def read_employees():
    employees = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees


# write employee data (after sorting)
def write_employees(employees):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Serial No", "Name", "Phone No", "ID Card No"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)


# add a new employee
def add_employee():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    id_card = input("Enter ID Card Number: ").strip()

    employees = read_employees()

    serial_no = len(employees) + 1

    employees.append({
        "Serial No": serial_no,
        "Name": name,
        "Phone No": phone,
        "ID Card No": id_card
    })

    # sort A–Z by Name
    employees.sort(key=lambda x: x["Name"].lower())

    # reassign serial numbers after sorting
    for index, emp in enumerate(employees, start=1):
        emp["Serial No"] = index

    write_employees(employees)
    print("Employee added successfully!")


# main program
initialize_file()

while True:
    print("\n1. Add Employee")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        break
    else:
        print("Invalid choice!")
