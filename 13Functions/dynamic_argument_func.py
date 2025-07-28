def carDetails(make, model, year, color, *features):
    print(f'Car Make: {make}')
    print(f'Car Model: {model}')
    print(f'Car Year: {year}')
    print(f'Car Color: {color}')
    print('Car Features:')
    for feature in features:
        print(f'- {feature}')


carDetails('Toyota', 'Camry', 2020, 'Blue', 'Sunroof', 'Leather Seats', 'Bluetooth')
carDetails('Honda', 'Civic', 2019, 'Red', 'Backup Camera', 'Navigation System')
carDetails('Ford', 'Mustang', 2021, 'Black', 'Sport Package', 'Premium Sound System', 'Heated Seats')
carDetails('Tesla', 'Model 3', 2022, 'White', 'Autopilot', 'Full Self-Driving Capability', 'Premium Interior')


print("*"*100)

def UserDetails(name, age, **user_info):
    print(f'User Name: {name}')
    print(f'User Age: {age}')
    for key, value in user_info.items():
        print(f'{key} is {value}')


UserDetails('Alice', 30, city='New York', occupation='Engineer', hobbies=['Reading', 'Traveling'])
UserDetails('Bob', 25, city='Los Angeles', occupation='Designer')
UserDetails('Charlie', 28, city='Chicago', occupation='Data Scientist', interests=['AI', 'Machine Learning'])
UserDetails('Diana', 22, city='Miami', occupation='Student', hobbies=['Photography', 'Cooking'], favorite_color='Blue')
