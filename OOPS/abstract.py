"""
ABSTRACT

-> An abstract class in Python is a class that cannot be instantiated and is meant to be subclassed. It defines a blueprint for other classes.
   Abstract classes typically contain one or more abstract methods, which must be implemented by subclasses.
   
Key Points About Abstract Classes :

-> Abstract classes cannot be instantiated directly.

-> They are created using ABC (Abstract Base Class).

-> Any method marked with @abstractmethod must be implemented by subclasses.

-> Abstract classes can have concrete (normal) methods along with abstract ones
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def start_engine(self):

        print("start engine")

    def stop_engine(self):

        print("stop engine")

    @abstractmethod
    def change_gear(self):

        pass

class Car(Vehicle):

    def change_gear(self):

        print("change gear")

class Truck(Vehicle):

    def change_gear(self):

        print("change gear")


c1 = Car()

c1.change_gear()

c1.start_engine()

c1.stop_engine()