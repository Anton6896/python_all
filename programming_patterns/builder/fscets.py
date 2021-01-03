
"""
have an person obj (for this example)
and have an 2 builders that have one main PersonBuilder
 interface for build person obj
"""


class Person:
    def __init__(self) -> None:
        super().__init__()

        print('creating instance of person .. ')

        # ADDRESS
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f"Address: ({self.street_address}, {self.postcode}, {self.city})\n" +\
            f"Employment info: ({self.company_name}, {self.position}, {self.annual_income})"


class PersonBuilder:
    # interface class 
    def __init__(self, person=None) -> None:
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    per1 = pb\
        .lives \
        .at('123 London st') \
        .in_city('London') \
        .with_postcode('123 432') \
        .works \
        .at('company 1') \
        .as_a('Manager') \
        .earning('23453') \
        .build()

    print(f'personn 1:  \n{per1}')

    per2 = PersonBuilder().build()
    print(f'person 2 : \n{per2}')
