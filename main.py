import csv

from menu import Menu
from manage import Manage
from employee import Employee
from address import Address


def get_company_data():
    file_name = "company.csv"

    with open(file_name, mode="r") as file:
        reader = csv.reader(file)

        # Read the first line for company details
        next(reader)
        company_details = next(reader)

        company_name = company_details[0]

        company_address = Address(
            street=company_details[1],
            number=company_details[2],
            city=company_details[3],
        )

        # Skip the second line (headers for employees)
        next(reader)

        # create the manage object
        manage_obj = Manage(
            company_name=company_name, address=company_address, employees=[]
        )

        # Read the employee details and create Employee objects
        for row in reader:
            print(row)
            # e_id, firstname, lastname, street, number, city, phone_number, gender = row
            e_id = row[0]
            firstname = row[1]
            lastname = row[2]
            street = row[3]
            number = row[4]
            city = row[5]
            phone_number = row[6]
            gender = row[7]

            address = Address(street=street, number=number, city=city)

            employee = Employee(
                e_id=e_id,
                firstname=firstname,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                gender=gender,
            )

            manage_obj.add_employee(employee)

        return manage_obj


def save_company_data(manage):
    file_name = "company_saved.csv"

    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "street", "number", "city"])

        # Write the company details
        company_name = manage.get_company_name()  # Access private attribute
        address = manage.get_address()  # Address object
        writer.writerow(
            [
                company_name,
                address.get_street(),
                address.get_number(),
                address.get_city(),
            ]
        )

        # Write the employee headers
        writer.writerow(
            ["id", "firstname", "lastname", "address", "phone_number", "gender"]
        )

        # Write the employee data
        for employee in manage.employees:
            writer.writerow(
                [
                    employee.get_e_id(),
                    employee.get_firstname(),
                    employee.get_lastname(),
                    str(employee.get_address()),  # Address as a string
                    employee.get_phone_number(),
                    employee.get_gender(),
                ]
            )


def print_company(manage):
    print(manage)


def print_employees(manage):
    manage.print_employee()


def add_new_employee(manage):
    extra_employee = Employee(
        e_id="007",
        firstname="James",
        lastname="Bond",
        address=Address("MI6", "007", "London"),
        phone_number="050-2345678",
        gender="M",
    )

    manage.add_employee(extra_employee)


def remove_employee(manage):
    extra_employee = Employee(
        e_id="007",
        firstname="James",
        lastname="Bond",
        address=Address("MI6", "007", "London"),
        phone_number="050-2345678",
        gender="M",
    )

    manage.remove_employee(extra_employee)


def exit_menu(manage):
    print("save the data before exit")
    save_company_data(manage)
    print("The data has been successfully saved.")
    print("Bye Bye!")
    exit()


def main():
    manage = get_company_data()
    menu_options = [
        ("Print company details", print_company, manage),
        ("Print all employees", print_employees, manage),
        ("Add new employee", add_new_employee, manage),
        ("Remove employee", remove_employee, manage),
        ("EXIT", exit_menu, manage),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == "__main__":
    main()
