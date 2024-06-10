class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __repr__(self):
        return 'A dog called ' + self.name 
    
    def speak(self):
        return (
            f'Hey, I am a dog. My name is {self.name}. ' 
            f'I am {self.age} years. I\'m a {self.breed}. ' 
            'Woof Woof!'
        )


class Person():
    def __init__(self, name, gender, marital_status, height):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.height = height

    def __repr__(self):
        return (
            f'A babe called {self.name} '
            f'{self.height} tall '
        )
      
     
    
    
