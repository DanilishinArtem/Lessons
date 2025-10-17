# Classes
### General
```python
# Example of creation atributes of the class without declaration in the class
class Cat():
    pass

if __name__ == "__main__":
    cat = Cat()
    cat.name = "Kitty"
    cat.surname = "Abramovich"
    print(f'[INFO] name: {cat.name}, surname: {cat.surname}')
```
### Class inheritance
```python
class Car():
    pass

class Yugo(Car):
    pass
```
### Method super()
```python
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

if __name__ == "__main__":
    bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
    print(f'[INFO] bob is subclass of Person: {issubclass(EmailPerson, Person)}')
    print(f'[INFO] name: {bob.name}, email: {bob.email}')
```
### Multiple inheritance
```python
class Animal:
    def says(self):
        return 'I speak!'
    
class Horse(Animal):
    def says(self):
        return 'Neigh!'
    
class Donkey(Animal):
    def says(self):
        return 'Hee-haw'
    
class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

if __name__ == "__main__":
    print(f'[INFO] Info about inherison of Mule: {Mule.mro()}')
    print(f'[INFO] Info about inherison of Hinny: {Hinny.mro()}')

    mule = Mule()
    hinny = Hinny()
    print(f'Mule says {mule.says()}')
    print(f'Hinny says {hinny.says()}')
# output
# [INFO] Info about inherison of Mule: [<class '__main__.Mule'>, <class '__main__.Donkey'>, <class '__main__.Horse'>, <class '__main__.Animal'>, <class 'object'>]
# [INFO] Info about inherison of Hinny: [<class '__main__.Hinny'>, <class '__main__.Horse'>, <class '__main__.Donkey'>, <class '__main__.Animal'>, <class 'object'>]
# Mule says Hee-haw
# Hinny says Neigh!
```
### Self is the first argument
```python
class Animal:
    def says(self):
        return 'I speak!'

if __name__ == "__main__":
    animal = Animal()
    print(Animal.says(animal))
```
### Privacy of the fields in classes
We can use Getter and Setter as an immitation of the privacy of fields of the class
```python
class Duck():
    def __init__(self, intput_name):
        self.hidden_name = intput_name
    def get_name(self):
        print(f'[DEBUG] inside getter')
        return self.hidden_name
    def set_name(self, input_name):
        print(f'[DEBUG] inside setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

if __name__ == "__main__":
    duck = Duck('Donald')
    duck.name
    duck.name = 'Donald'
```
We also can use decorators for imitate getter and setters
```python
class Duck():
    def __init__(self, intput_name):
        self.hidden_name = intput_name
    @property
    def name(self):
        print(f'[DEBUG] inside getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print(f'[DEBUG] inside setter')
        self.hidden_name = input_name

if __name__ == "__main__":
    duck = Duck('Donald')
    duck.name
    duck.name = 'Donald'
```
Also we can use Getter as an calculational method
```python
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

if __name__ == "__main__":
    circle = Circle(2)
    print(circle.diameter)
```
For privacy we can change internal names of the class
```python
class Duck():
    def __init__(self, name):
        # __variable: internal variable
        self.__name = name
    @property
    def name(self):
        print(f'[DEBUG] Inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print(f'[DEBUG] Inside the setter')
        self.__name = input_name

if __name__ == "__main__":
    duck = Duck('Donald')
    duck.name
    duck.name = 'Duck'
```
### Methods for the whole class
Shown example for creation of the counter of the classes by using common variable and inherinson
```python
class Base:
    counter = 0
    def __init__(self):
        A.counter += 1
    def show_counter(cls):
        print(f'[DEBUG] Total counter: {cls.counter}')

class A(Base):
    pass

if __name__ == "__main__":
    first = A()
    second = A()
    third = A()

    print(f'[INFO] first.counter: {first.counter}, \
            second.counter: {second.counter}, \
                third.counter: {third.counter}')
    first.show_counter()
    second.show_counter()
    third.show_counter()
# Output:
# [INFO] first.counter: 3, second.counter: 3, third.counter: 3
# [DEBUG] Total counter: 3
# [DEBUG] Total counter: 3
# [DEBUG] Total counter: 3
```
Shown a second way to realization of the inherits counter
```python
class A:
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A")
    # The second method of info counter
    @classmethod
    def kids_1(cls):
        print(f'[INFO] A has {cls.count} little objects')
    # The first method of info counter
    @staticmethod
    def kids_2():
        print(f'[INFO] A has {A.count} little objects')

if __name__ == "__main__":
    easy_a = A()
    breezy_a = A()
    wheezy_a = A()
    A.kids_1()
    A.kids_2()
```
### Magical methods
Table 1. Magical methods for comparison
| Magical Method | Action |
|--------------|--------------|
| __eq__(self, other) | self == other |
| __ne__(self, other) | self != other |
| __lt__(self, other) | self < other |
| __gt__(self, other) | self > other |
| __le__(self, other) | self <= other |
| __ge__(self, other) | self >= other |

Table 2. Magical methods for comparison
| Magical Method | Action |
|--------------|--------------|
| __add__(self, other) | self + other |
| __sub__(self, other) | self - other |
| __mul__(self, other) | self * other |
| __floordiv__(self, other) | self // other |
| __truediv__(self, other) | self / other |
| __mod__(self, other) | self % other |
| __pow__(self, other) | self ** other |
### Dataclasses
```python
from dataclasses import dataclass

@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

if __name__ == "__main__":
    snowman = AnimalClass('yeti', 'Himalayas', 46)
    duck = AnimalClass(habitat='lake', name='duck')
    print(f'[Snowman] name: {snowman.name}, habitat: {snowman.habitat}, teeth: {snowman.teeth}')
    print(f'[Duck] name: {duck.name}, habitat: {duck.habitat}, teeth: {duck.teeth}')

# Output:
# [Snowman] name: yeti, habitat: Himalayas, teeth: 46
# [Duck]    name: duck, habitat: lake,      teeth: 0
```