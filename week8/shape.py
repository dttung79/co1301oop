from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    @abstractmethod
    def area(self): # we don't know how to calculate the area of a shape, so make it abstract
        pass
    
    # override the __str__ method to return the name and area of the shape
    def __str__(self) -> str:
        return f'{self.name}, area: {self.area}'