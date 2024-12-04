import csv

from menu import Menu


def get_company_data():
    file_name = "company.csv"


def save_company_data(manage):
    pass


def print_company(manage):
    pass


def print_employees(manage):
    pass


def add_new_employee(manage):
    pass


def remove_employee(manage):
    pass


def exit_menu(manage):

    print("Bye Bye!")
    exit()


def main():
    manage = get_company_data()
    menu_options = [
        ('Print company details', print_company, manage),
        ('Print all employees', print_employees, manage),
        ('Add new employee', add_new_employee, manage),
        ('Remove employee', remove_employee, manage),
        ('EXIT', exit_menu, manage),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == '__main__':
    main()
