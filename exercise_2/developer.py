from .employee import Employee


class Developer(Employee):
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
        programming_languages,
        experience_years=0,
    ):
        super().__init__(
            e_id, firstname, lastname, address, phone_number, gender, salary, seniority
        )
        self.__programming_languages = (
            programming_languages
            if self.contains_valid_language(programming_languages)
            else None
        )
        self.__experience_years = self.validate_experience_years(experience_years)

    VALID_LANGUAGES = {"Go", "Java", "Python"}

    @staticmethod
    def contains_valid_language(programming_languages):
        if not programming_languages:
            return False

        for item in programming_languages:
            if item in Developer.VALID_LANGUAGES:
                return True

        return False

    @staticmethod
    def validate_experience_years(experience_years):
        if experience_years < 0:
            return 0

        return experience_years

    def __str__(self):
        return (
            f" <{self.__class__.__name__}> :{self._e_id}, {self._firstname}, {self._lastname}, {self._email}, "
            f"{self._address}, {self._phone_number}, {self._gender}, {self.__salary}, {self.__seniority}, {self.__programming_languages}, {self.__experience_years}"
        )

    def __eq__(self, other):
        if isinstance(other, Developer):
            return self._e_id == other.get_e_id()

        return False

    def __add__(self, programming_language):
        if (
            isinstance(programming_language, str)
            and programming_language in Developer.VALID_LANGUAGES
            and programming_language not in self.__programming_languages
        ):
            self.__programming_languages.append(programming_language)

    def __sub__(self, programming_language):
        if (
            isinstance(programming_language, str)
            and programming_language in self.__programming_languages
            and len(self.__programming_languages) > 1
        ):
            self.__programming_languages.remove(programming_language)

    def __gt__(self, other):
        if isinstance(other, Developer):
            return len(self.__programming_languages) > len(
                other.__programming_languages
            )

        return False

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_seniority(self):
        return self.__seniority

    def set_seniority(self, seniority):
        self.__seniority = seniority
