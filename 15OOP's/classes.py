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


Emp1 = Employee("John Doe", "johndee@gmail.com", 30, "Software Engineer", "New York")
Emp2 = Employee("Jane Smith", "janesmith@gmail.com", 28, "Data Scientist", "San Francisco")
Emp3 = Employee("Alice Johnson", "alicejohnson@gmail.com", 35, "Project Manager", "Los Angeles")

Emp1.display()
Emp2.display()
Emp3.display()