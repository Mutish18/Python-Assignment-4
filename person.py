class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")


person_instance = Person("Benjamin", 22, "Male")

# Call the introduce method
person_instance.introduce()
