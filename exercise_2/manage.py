class Manage:
    def __init__(self, company_name, address, employees):
        self.__company_name = company_name
        self._address = address
        self.employees = employees if employees else []

    def __str__(self):
        return f"Manage:{self.__company_name}, {self._address}"

    def __repr__(self):
        return f"Manage:{self.__company_name}, {self._address}"

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            return True
        return False

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return True
        return False

    def print_employee(self):
        if self.employees:
            print("employees:")
            for employee in self.employees:
                print(employee)
        else:
            print("no employees in the company")

    def get_company_name(self):
        return self.__company_name

    def get_address(self):
        return self._address

    def __getitem__(self, e_id):
        for employee in self.employees:
            if employee.get_e_id() == e_id:
                return employee

        return None
