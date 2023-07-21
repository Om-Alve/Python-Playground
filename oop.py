class Parent:

    def __init__(self, name, age):
        self.age = age
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)


om = Child("Om", 18)

print(om.name)
print(om.age)
