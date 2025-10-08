# Variables
### type(a)
```
show type of variable;
```
### isinstance(a, int)
```
Show wether the variable point to an object of a certain type;
```
### Using "\\"
```
We can continue string by using "\\" (Example: sum = 1 + \\
                                                     2 + \\
                                                     3 + \\
                                                     4)
```
### Warlus operator (:=)
```python
tweet_limit = 250
tweet_string = "Blah" * 50
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print("A fitting tweet {}".format(diff))
else:
    print("Went over by", abs(diff))
```
### Quotation marks
```
[1] We can use "this string" or 'this string', two types of quotation marks, this is the way to use quotation marks inside of the quotation marks.
    Example:  message = "'Nay' and 'Way' are the best friends"
[2] Triple quotation marks are used for long texts. Example: message = '''I do not like thee, Doctor Fell. The reason why, I cannot tell.'''
```
### Strings
```
[1] \n - new string, \t - tabulation, ...
[2] Indexing: [:], [start:], [:end], [start:end], [start:end:step]
[3] split: message = "get gloves, get mask, give cat vitamins, call ambulance" => message.split(',')
[4] join: message = ['one','two','three'] => message = ', '.join(message)
[5] replace: message.replace('one', 'two')
[6] strip (delete): message.strip('a')
[7] search: startswith, endswith, find, index, upper, lower
[8] alignment: center, ljust, rjust. Example: f'The {thing.capitalize()} is in the {place.rjust(20)}'
```
### For, while loops
```
[1] We can break "for" loop by using "break"
[2] We can "pass" current step of the loop by using "continue"
[3] Generate numeric array: for x in range(0,3): print(x), where range(start,end,step)
```
### Tuples, lists
```
[1] empty_tuple = ('one',)
    we can assign several variables: marx_tuple = ('one','two','three') => a, b, c = marx_tuple
    Tuples can be concatinated: ('one',) + ('two','three')
    Tuples are unchangable!
[2] Lists
Extend list:
    x = ['one','two']; y = ['three','four']; x.extend(y)
Concatinate lists:
    x = ['one','two']; y = ['three','four']; x + y
Remove element:
    x.remove('one')
Pop element:
    x.pop(1) - we pass the index of the element as an argument
Clear:
    x.clear() - clear whole the list
Find the index:
    x.index('one')
Count: to count number of elements
Sort elements of the list: x = [1,2,6,3,5]
    y = sorted(x) - we can get the copy of sorted list
    x.sort() - we change the list by sorting
Copy: can can copy by using different methods: 
                                                1. b = a.copy(); 
                                                2. b = list(a); 
                                                3. b = a[:]
Deepcopy: if we have changable elements in the list we should use deepcopy:
    x = [1,2,[3,4]]
    y = x.copy() - after changing smth like this (x[2][1]=10) element of the y list also be changed
    import copy
    y = copy.deepcopy(x) - correct way for copy for changable elements of the list
Iterating through several lists:
    days = ['monday','tuesday','wednesday']
    fruits = ['banana','orange','peach']
    drinks = ['coffee','tea','beer']
    desserts = ['tiramisu','ice cream','pie','pudding']
    for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
        print(f'day: {day}, fruit: {fruit}, drink: {drink}, dessert: {desser}')
We also can create a list by using zip:
    list(zip(days, fruits))
Creating list by using for:
    numbers = [number-1 for number in range(1,6)]
```
### Dict
```
Convert list to dict:
    x = [['a','b'],['c','d'],['e','f']]
    x = dict(x) => {'a': 'b', 'c': 'd', 'e': 'f'}
To get element by key:
    x.get('a', 'default value')
    if we not assign default value we will get None if there is no key in the dict: x.get('z') => None
To get keys, values, items:
    x.keys()
    x.values()
    x.items()
Join dicts:
    [1]:
        first = {'a': 'agony', 'b': 'bliss'}
        second = {'b': 'bagels', 'c': 'candy'}
        total = {**first, **second}
    [2]:
        first.update(second)
Del, Pop and clear:
    del first['a']
    temp = first.pop('a')
    first.clear()
Dict also has copy and deepcopy methods
```
### Set
```
Creating:
    x = set()
    x = {1,2,3,3,3,4} => {1, 2, 3, 4}
Methods:  Add, Remove
To create frozen set:
    x = frozenset([1,2,3])
    x.add(5) - AttributeError: 'frozenset' object has no attribute 'add'
```

# Functions
### Positional arguments
```python
def menu(wine, entree, dessert):
    return {'wine': wine,'entree': entree,'dessert': dessert}
menu('bordeaux','beef','bagel')
```
### By using default values for arguments
```python
def menu(entree='beef', dessert='bagel', wine='bordeaux'):
    return {'wine': wine,'entree': entree,'dessert': dessert}
menu(entree='pork')

# Example of incorrent using default arguments
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

if __name__ == "__main__":
    buggy('hi')
    buggy('my')

# outout: 
        # ['hi']
        # ['hi', 'my']

# So here is correct code of the function:
def buggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
```
### Arguments by using " * "
```python
# We can use " * " only for arguments description and for calling some function
def foo(*args):
    print(f'Args: {args}')

if __name__ == "__main__":
    foo(1,2,3,'hello')
    args = (1,2,3,'hello')
    foo(*args)
```
### Arguments by using " ** "
```python
def foo(**kwargs):
    print(f'kwargs: {kwargs}')

if __name__ == "__main__":
    foo(entree='beef', dessert='bagel', wine='bordeaux')
    kwargs = {'entree':'beef', 'dessert':'bagel', 'wine':'bordeaux'}
    foo(**kwargs)
```
### Naming args
```python
# Symbol " * " indicate that we can use parameters "start", "end" only as naming arguments
def foo(data, *, start=0, end=100):
    for value in data[start:end]:
        print(value)

if __name__ == "__main__":
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    foo(data)
    foo(data, start=0, end=3)
```
### Strings of documentation
```python
def foo(anything):
    'foo function return its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Print the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

# If we want to show documentation of the function we can use "help" or foo.__doc__
if __name__ == "__main__":
    help(print_if_true)
    print(print_if_true.__doc__)
```
### Inner functions
```python
def foo(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
```
### Closures
```python
# foo function remember the "saying" variable, that can be used through calling foo function which was returned by calling knights function.
def knights(saying):
    def foo():
        return f"We are the knights who say: {saying}"
    return foo

if __name__ == "__main__":
    func = knights("Hello")
    print(func())
```
### Lambda functions
Signature:
Lambda function with one argument:
```python
double = lambda x: x*2
```
Lambda function with several arguments
```python
foo = lambda x, y, z: x + y + z
```
Example:
```python
def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word):
    return word.capitalize() + '!'

if __name__ == "__main__":
    stairs = ['thud','meow','thud','hiss']
    # First way to use edit_story function:
    edit_story(stairs, enliven)
    # Second way to use edit_story function:
    edit_story(stairs, lambda word: word.capitalize() + '!')
```
### Generators
#### Generator is an object that create sequences
```python
# Creation generator through function:
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

if __name__ == "__main__":
    for item in my_range(1, 5):
        print(item)

# Another method for creating generator:
my_array = (pair for pair in zip(['a','b'],['1','2']))
for thing in my_array:
    print(thing)
```
### Decorators
```python
def decorator(foo):
    def info(*args, **kwargs):
        print(f'Name: {foo.__name__}')
        return foo(*args, **kwargs)
    return info

@decorator
def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(sub(10, 6))
```
### Local and global variables
```python
animal = 'wombat'

def change_local_1():
    animal = 'wombat'
    print(f'[INFO] inside change_local: {animal}, id: {id(animal)}')

def change_local_2():
    animal = 'fruitbat'
    print(f'[INFO] inside change_local: {animal}, id: {id(animal)}')

def change_global_1():
    print(f'[INFO] First calling of the global variable ---> ERROR {animal}')
    animal = 'fruitbat'
    print(f'[INFO] inside change_local: {animal}, id: {id(animal)}')

def change_global_2():
    global animal
    print(f'[INFO] First calling of the global variable ---> WITHOUT ERROR {animal}')
    animal = 'fruitbat'
    print(f'[INFO] inside change_local: {animal}, id: {id(animal)}')

if __name__ == "__main__":
    print(f'[INFO] outside change_local: {animal}, id: {id(animal)}')
    change_local_1()
    # --- output of the program (the same addresses)---
    # [INFO] outside change_local: wombat, id: 140656527905712
    # [INFO] inside change_local: wombat,  id: 140656527905712
    print(f'[INFO] outside change_local: {animal}, id: {id(animal)}')
    change_local_2()
    # --- output of the program (NOT the same addresses)---
    # [INFO] outside change_local: wombat,  id: 140578532774832
    # [INFO] inside change_local: fruitbat, id: 140578530595440

    # Wrong function ----->
    # change_global_1()

    # Correct function --->
    change_global_2()
```
We can check local and global variable spaces by using:
- locals()
- globals()
### Recursions
```python
def my_flatten(args):
    for item in args:
        if isinstance(item, list):
            for subitem in my_flatten(item):
                yield subitem
        else:
            yield item

if __name__ == "__main__":
    lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
    print(list(my_flatten(lol)))
```
### Exceptions (try, except)
```python
# One Exceptions ---------->
if __name__ == "__main__":
    short_list = [1, 2, 3]
    positioin = 5
    try:
        print(f'[INFO] short_list[{positioin}] = {short_list[positioin]}')
    except:
        print(f'[ERROR] Need a position between 0 and {len(short_list)-1} but got {positioin}')

# Several Exceptions ---------->
if __name__ == "__main__":
    short_list = [1, 2, 3]
    value = input(f'Position [q to quit]?')
    while True:
        if value == 'q':
            break
        try:
            position = int(value)
            print(f'[INFO] Output: {short_list[position]}')
        except IndexError as err:
            print(f'[ERROR] Bad index: {position}')
        except Exception as other:
            print(f'[ERROR] Something else broke: {other}')
        break
```