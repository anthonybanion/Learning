
# Dictionaries are mutable, unordered collections of key-value pairs.
# The key for dictionaries must be unique and immutable 
# {int, float, bool, str, tuple}

user = {
    'name': 'Anthony',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science'],
    'address': {
        'street': '123 Main St',
        'city': 'New York'
    },
    'phone_numbers': ['123-456-7890', '987-654-3210']
}

print(user)