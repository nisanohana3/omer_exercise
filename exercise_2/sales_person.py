from .employee import Employee


class Salesperson(Employee):
    def __init__(
        self,
        e_id,
        firstname,
        lastname,
        address,
        phone_number,
        gender,
        salary,
        seniority,
        sales_target,
        current_sales=0,
    ):
        super().__init__(
            e_id, firstname, lastname, address, phone_number, gender, salary, seniority
        )
        self.__sales_target = sales_target
        self.__current_sales = self.validate_current_sales(current_sales)

    sales = 0

    @staticmethod
    def validate_current_sales(current_sales):
        if current_sales < 0:
            return 0

        return current_sales

    def __str__(self):
        return (
            f" <{self.__class__.__name__}> :{self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}, {self.__salary}, {self.__seniority}, {self.__sales_target}, {self.__current_sales}"
        )

    def __eq__(self, other):
        if isinstance(other, Salesperson):
            return self._e_id == other.get_e_id()

        return False

    def __add__(self, sales_number):
        if isinstance(sales_number, int):
            self.__current_sales += sales_number
            Salesperson.sales += sales_number

    def __gt__(self, other):
        if isinstance(other, Salesperson):
            return len(self.__current_sales) > len(other.__current_sales)

        return False

    def __mod__(self, sales_number):
        if isinstance(sales_number, int):
            return (self.__current_sales // sales_number) * 100

    def get_sales_target(self):
        return self.__sales_target
