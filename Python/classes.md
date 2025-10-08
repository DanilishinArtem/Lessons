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