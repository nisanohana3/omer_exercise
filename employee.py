class Employee:
    def __init__(self, e_id, firstname, lastname, email, adress, phone_number, gender):
        self._e_id = e_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = f"{firstname}.{lastname}@gmail.com"
        self._adress = adress
        self._phone_number = self.validate_phone(phone_number)
        self._gender = self.validate_gender(gender)

    def id_e(self):
        return self._e_id

    

    def validate_phone(phone_number):
        if isinstance(phone_number,str) and phone_number.startswith("05") and len(phone_number)==10 and phone_number[2:].isdigit():
            return phone_number

    def validate_gender(gender):
        return gender if gender in ["M","F"] else None



