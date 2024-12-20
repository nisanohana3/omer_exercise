import csv

from menu import Menu
from .sales_person import Salesperson
from .developer import Developer
from .address import Address
from .manage import Manage


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

        # Create the manage object
        manage_obj = Manage(
            company_name=company_name, address=company_address, employees=[]
        )

        # Read the employee details and create corresponding objects
        for row in reader:
            role = row[0]

            e_id = row[0]
            firstname = row[1]
            lastname = row[2]
            street = row[3]
            number = row[4]
            city = row[5]
            phone_number = row[6]
            gender = row[7]
            salary = row[8]
            seniority = row[9]
            param1 = row[10]
            param2 = row[11]

            address = Address(street=street, number=number, city=city)

            if role == "Developer":
                employee = Developer(
                    e_id=e_id,
                    firstname=firstname,
                    lastname=lastname,
                    address=address,
                    phone_number=phone_number,
                    gender=gender,
                    salary=salary,
                    seniority=seniority,
                    programming_languages=param1,
                    experience_years=param2,
                )
            elif role == "Salesperson":
                employee = Salesperson(
                    e_id=e_id,
                    firstname=firstname,
                    lastname=lastname,
                    address=address,
                    phone_number=phone_number,
                    gender=gender,
                    salary=salary,
                    seniority=seniority,
                    sales_target=param1,
                    current_sales=param2,
                )

            else:
                print("Invalid role")

            manage_obj.add_employee(employee)

        return manage_obj


def save_company_data(manage):
    file_name = "company_saved.csv"

    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the company details header
        writer.writerow(["name", "street", "number", "city"])

        # Write the company details
        company_name = manage.get_company_name()
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
            [
                "role",
                "id",
                "firstname",
                "lastname",
                "street",
                "number",
                "city",
                "phone_number",
                "gender",
                "salary",
                "seniority",
                "param1",
                "param2",
            ]
        )

        # Write the employee data
        for employee in manage.employees:
            address = employee.get_address()
            if isinstance(employee, Developer):
                writer.writerow(
                    [
                        "Developer",
                        employee.get_e_id(),
                        employee.get_firstname(),
                        employee.get_lastname(),
                        address.get_street(),
                        address.get_number(),
                        address.get_city(),
                        employee.get_phone_number(),
                        employee.get_gender(),
                        employee.get_salary(),
                        employee.get_seniority(),
                        ";".join(employee.get_programming_languages()),  # param1
                        employee.get_experience_years(),  # param2
                    ]
                )
            elif isinstance(employee, Salesperson):
                writer.writerow(
                    [
                        "Salesperson",
                        employee.get_e_id(),
                        employee.get_firstname(),
                        employee.get_lastname(),
                        address.get_street(),
                        address.get_number(),
                        address.get_city(),
                        employee.get_phone_number(),
                        employee.get_gender(),
                        employee.get_salary(),
                        employee.get_seniority(),
                        employee.get_sales_target(),  # param1
                        employee.get_current_sales(),  # param2
                    ]
                )

        print(f"Company data successfully saved to {file_name}")


def print_company(manage):
    print(manage)


def print_employees(manage):
    manage.print_employee()


# todo : add new fields to employee - create dev or salesperson according to role given
def add_new_employee(manage):
    role = input("Enter the role of the employee (Developer/Salesperson): ").strip()

    the_new_employee_id = input(
        "Enter the information of the employee that you want to add: \nPut ID: "
    )
    new_f_name = input("Put the first name: ")
    new_l_name = input("Put the last name: ")
    new_street = input("Put the address: \nPut the street: ")
    new_number = input("Put the number: ")
    new_city = input("Put the city: ")
    temp_address = Address(new_street, new_number, new_city)
    new_phone_number = input("Put the phone number: ")
    new_gender = input("Put the gender of the employee: ")
    new_salary = float(input("Put the salary: "))
    new_seniority = int(input("Put the seniority: "))

    if role.lower() == "developer":
        programming_languages = input(
            "Enter the programming languages (separated by ';'): "
        ).split(";")
        experience_years = int(input("Enter the experience years: "))
        new_employee = Developer(
            e_id=the_new_employee_id,
            firstname=new_f_name,
            lastname=new_l_name,
            address=temp_address,
            phone_number=new_phone_number,
            gender=new_gender,
            salary=new_salary,
            seniority=new_seniority,
            programming_languages=programming_languages,
            experience_years=experience_years,
        )
    elif role.lower() == "salesperson":
        sales_target = int(input("Enter the sales target: "))
        current_sales = int(input("Enter the current sales: "))
        new_employee = Salesperson(
            e_id=the_new_employee_id,
            firstname=new_f_name,
            lastname=new_l_name,
            address=temp_address,
            phone_number=new_phone_number,
            gender=new_gender,
            salary=new_salary,
            seniority=new_seniority,
            sales_target=sales_target,
            current_sales=current_sales,
        )
    else:
        print("Invalid role. Employee not added.")
        return

    if not manage.add_employee(new_employee):
        print("Employee already exists.")
    else:
        print(f"{role} successfully added!")


def remove_employee(manage):
    delete_employee = input(
        "enter the id of the employee you want to delete from the employee list:"
    )
    success = manage.remove_employee(delete_employee)
    if success is False:
        print("The employee was not in the employee list")


def add_programming_language(manage):
    developer_id = input("Enter the e_id of the developer:")
    lang_to_add = input("Enter the programming language to add:")

    devloper = manage[developer_id]

    devloper + lang_to_add


def remove_programming_language(manage):
    developer_id = input("Enter the e_id of the developer:")
    lang_to_add = input("Enter the programming language to add:")

    devloper = manage[developer_id]

    devloper - lang_to_add


def compare_developers(manage):
    dev1_id = input("Enter the e_id of the developer:")
    dev2_id = input("Enter the e_id of the developer:")

    dev1 = manage[dev1_id]
    dev2 = manage[dev2_id]

    if dev1 > dev2:
        print(f"{dev1.get_firstname()} is better than {dev2.get_firstname()}")
    else:
        print(f"{dev2.get_firstname()} is better than {dev1.get_firstname()}")


def compare_salesperson(manage):
    sale1_id = input("Enter the e_id of the sales person:")
    sale2_id = input("Enter the e_id of the sales person:")

    sale1 = manage[sale1_id]
    sale2 = manage[sale2_id]

    if sale1 > sale2:
        print(f"{sale1.get_firstname()} is better than {sale2.get_firstname()}")
    else:
        print(f"{sale2.get_firstname()} is better than {sale1.get_firstname()}")


def add_sales(manage):
    sales_person_id = input("Enter the e_id of the developer:")
    sales_number = int(input("Enter the sales amount to add (Must be a number):"))

    sales_person = manage[sales_person_id]

    sales_person + sales_number


def get_sales_target(manage):
    sales_person_id = input("Enter the e_id of the developer:")

    sales_person = manage[sales_person_id]

    print(f"Sales target of this person is {sales_person.get_sales_target()}")


def exit_menu(manage):
    save_company_data(manage)
    print("Bye Bye!")
    exit()


def main():
    manage = get_company_data()
    menu_options = [
        ("Print company details", print_company, manage),
        ("Print all employees", print_employees, manage),
        ("Add new employee", add_new_employee, manage),
        ("Remove employee", remove_employee, manage),
        ("Add programming language to developer", add_programming_language, manage),
        (
            "Remove programming language from developer",
            remove_programming_language,
            manage,
        ),
        ("Compare 2 developers", compare_developers, manage),
        ("Add sales to salesperson", add_sales, manage),
        ("Get sales target of salesperson", get_sales_target, manage),
        ("Compare 2 salesperson", compare_salesperson, manage),
        ("EXIT", exit_menu, manage),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == "__main__":
    main()
