import csv

from menu import Menu


def get_company_data():
    file_name = "company.csv"


def save_company_data(manage):
    csv_filename = "company.csv"


def print_company(manage):
    pass


def print_employees(manage):
    pass


def add_new_employee(manage):
    pass


def remove_employee(manage):
    pass


def add_programming_language(manage):
    pass


def remove_programming_language(manage):
    pass


def compare_developers(manage):
    pass


def compare_salesperson(manage):
    pass

def add_sales(manage):
    pass


def get_sales_target(manage):
    pass


def exit_menu(manage):
    save_company_data(manage)
    print("Bye Bye!")
    exit()


def main():
    manage = get_company_data()
    menu_options = [
        ('Print company details', print_company, manage),
        ('Print all employees', print_employees, manage),
        ('Add new employee', add_new_employee, manage),
        ('Remove employee', remove_employee, manage),
        ('Add programming language to developer', add_programming_language, manage),
        ('Remove programming language from developer', remove_programming_language, manage),
        ('Compare 2 developers', compare_developers, manage),
        ('Add sales to salesperson', add_sales, manage),
        ('Get sales target of salesperson', get_sales_target, manage),
        ('Compare 2 salesperson', compare_salesperson, manage),
        ('EXIT', exit_menu, manage),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == '__main__':
    main()
