class Manage:
    def __init__(self, company_name, address, employees):
        self.__company_name = company_name
        self._address = address
        self.employees = employees if employees is not None else []

     def __str__(self):
         return f"Manage :{self.__company_name}, {self.address}"

    def __repr__(self):
        return f"company(company_name = {self.__company_name},address = {self._address}, emplyees ={self.employees})"

    def employee_add(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            return  True
        return False

    def employee_remove(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return True
        return False

    def employee_print(self):
        if self.employees:
            print("employees:")
            for employee in self.employees:
                print(employee)
        else:
            print("no employees in the company")