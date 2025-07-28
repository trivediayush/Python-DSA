class Employee:
    def __init__(self, name, email, age, degination, city):
        self.name = name
        self.email = email
        self.age = age
        self.degination = degination
        self.city = city

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Designation: {self.degination}")
        print(f"City: {self.city}")

    def new_city(self, new_City):
        self.city = new_City
        print(f'City updated to: {self.city}s')

