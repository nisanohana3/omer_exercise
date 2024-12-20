from .person import Person


class Employee(Person):
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
    ):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender)
        self.__salary = salary
        self.__seniority = seniority

    def __repr__(self):
        return (
            f" <{self.__class__.__name__}> : {self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}, {self.__salary}, {self.__seniority}"
        )

    def __str__(self):
        return (
            f" <{self.__class__.__name__}> :{self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}, {self.__salary}, {self.__seniority}"
        )

    def __eq__(self, other):
        if isinstance(other, Person):
            return self._e_id == other.get_e_id()  # Equality based on e_id

        return False

    # def __hash__(self):
    #     return hash(self._e_id)

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_seniority(self):
        return self.__seniority

    def set_seniority(self, seniority):
        self.__seniority = seniority
