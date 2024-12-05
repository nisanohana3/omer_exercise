class Employee:
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender):
        self._e_id = e_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = self._generate_email(firstname, lastname)
        self._address = address
        self._phone_number = self._validate_phone(phone_number)
        self._gender = self._validate_gender(gender)

    @staticmethod
    def _validate_phone(phone_number):
        if (
            isinstance(phone_number, str)
            and phone_number.startswith("05")
            and len(phone_number) == 11
            and phone_number[3] == "-"
            and phone_number[0:2].isdigit()
            and phone_number[4:].isdigit()
        ):
            return phone_number

        return None

    @staticmethod
    def _validate_gender(gender):
        return gender if gender in ["M", "F"] else None

    @staticmethod
    def _generate_email(firstname, lastname):
        return f"{firstname}.{lastname}@email.com"

    def __repr__(self):
        return (
            f"{self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}"
        )

    def __str__(self):
        return (
            f"{self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}"
        )

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self._e_id == other.get_e_id()  # Equality based on e_id

        return False

    def __hash__(self):
        return hash(self._e_id)

    def get_e_id(self):
        return self._e_id
