my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print(len(my_dict))
print(type(my_dict))
print(my_dict)
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict.get('age')}")
my_dict['age'] = 31
print(f"Updated Age: {my_dict['age']}")
my_dict['country'] = 'USA' 
print(f"Added Country: {my_dict['country']}")
print(my_dict)