class Employee:
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender):
        self.__e_id = e_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = self.generate_email(firstname, lastname)
        self.__address = address
        self.__phone_number = self.validate_phone(phone_number)
        self.__gender = self.validate_gender(gender)

    def id_e(self):
        return self.__e_id

    @staticmethod
    def validate_phone(phone_number):
        if (
            isinstance(phone_number, str)
            and phone_number.startswith("05")
            and len(phone_number) == 10
            and phone_number[2:].isdigit()
        ):
            return phone_number

        return None

    @staticmethod
    def validate_gender(gender):
        return gender if gender in ["M", "F"] else None

    @staticmethod
    def generate_email(firstname, lastname):
        return f"{firstname.lower()}.{lastname.lower()}@email.com"

    def get_e_id(self):
        return self.__e_id

    def __repr__(self):
        return (
            f"{self.__e_id}, {self.__firstname}, {self.__lastname}, {self.__email}, "
            f"{self.__address}, {self.__phone_number}, {self.__gender}"
        )

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.__e_id == other.get_e_id()  # Equality based on e_id
        return False

    def __hash__(self):
        return hash(self.e_id)
