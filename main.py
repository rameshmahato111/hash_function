# hash() for Custom Objects by overriding __hash__()
# hash() method internally calls __hash__() method.
# So, any objects can override __hash__() for custom hash values.

# But for correct hash implementation, __hash__() should always return an integer.
# And, both __eq__() and __hash__() methods have to be implemented.


import hashlib
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        print('The hash is:')
        return hash((self.name, self.age))

person = Person('Nepal', 22)
print(hash(person))
