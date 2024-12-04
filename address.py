class Address:
    def __init__(self, street, number, city):
        self.__street = street
        self.__number = number
        self.__city = city

    def __str__(self):
        return f"{self.__street}, {self.__number}, {self.__city}"

    def __repr__(self):
        return f"address(street = {self.__street}, number = {self.__number}, city = {self.__city}"

    def get_street(self):
        return self.__street

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city
        
