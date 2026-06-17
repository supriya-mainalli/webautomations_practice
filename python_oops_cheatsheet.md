# Python OOP Cheatsheet for SDET Interviews

> Quick reference covering all 8 OOP concepts with sample code and interview tips.

---

## Table of Contents

1. [Class & Object](#1-class--object)
2. [Inheritance](#2-inheritance)
3. [Polymorphism](#3-polymorphism)
4. [Encapsulation](#4-encapsulation)
5. [Abstraction](#5-abstraction)
6. [Magic Methods (Dunder)](#6-magic-methods-dunder)
7. [Properties (getter/setter)](#7-properties-gettersetter)
8. [Class method vs Static method](#8-class-method-vs-static-method)

---

## 1. Class & Object

> **Blueprint (class) vs instance (object). `__init__` is the constructor.**

```python
class Car:
    # class variable - shared by ALL instances
    wheels = 4

    def __init__(self, brand, speed):
        # instance variables - unique per object
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} goes {self.speed}kmh"


# Creating objects (instances)
car1 = Car("Toyota", 120)
car2 = Car("BMW", 200)

print(car1.describe())  # Toyota goes 120kmh
print(car2.describe())  # BMW goes 200kmh
print(Car.wheels)       # 4 (class variable)
```

### Key Concepts

| Term | Meaning |
|---|---|
| `self` | Refers to the current instance. Always first param in instance methods |
| `__init__` | Constructor — runs automatically when object is created |
| Class variable | Shared across all instances (`wheels = 4`) |
| Instance variable | Unique per object (`brand`, `speed`) |

> **Interview tip:** "A class is a blueprint, an object is a specific instance of that blueprint with its own state."

---

## 2. Inheritance

> **Child class inherits attributes and methods from parent class.**

```python
class Animal:          # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def breathe(self):
        return "inhale/exhale"


class Dog(Animal):     # Child inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # call parent __init__
        self.breed = breed

    def speak(self):            # override parent method
        return f"{self.name} says Woof!"


dog = Dog("Rex", "Labrador")
print(dog.speak())    # Rex says Woof!
print(dog.breathe())  # inhale/exhale (inherited from Animal)
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
```

### Types of Inheritance

```python
# Single inheritance
class Dog(Animal): ...

# Multiple inheritance
class Amphibian(Land, Water): ...

# Multilevel inheritance
class Animal: ...
class Dog(Animal): ...
class Puppy(Dog): ...
```

> **Interview tip:** "`super()` lets me call the parent class method without hardcoding the parent name — important in multiple inheritance."

---

## 3. Polymorphism

> **Same method name, different behaviour depending on the object.**

### Method Overriding

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2


# Polymorphism in action — same method, different behaviour
shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())  # 78.5, then 16
```

### Duck Typing (Python style)

```python
# No inheritance needed!
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

def make_sound(animal):
    print(animal.speak())  # works for both!

make_sound(Dog())  # Woof
make_sound(Cat())  # Meow
# "If it has .speak(), it works!"
```

> **Interview tip:** "Polymorphism means the same interface works for different types. In Python, duck typing means I don't even need inheritance — if the object has the method, it works."

---

## 4. Encapsulation

> **Hiding internal data. Control access using public, protected, private.**

```python
class BankAccount:
    def __init__(self, balance):
        self.owner = "Supriya"    # public
        self._limit = 10000       # protected (convention)
        self.__balance = balance  # private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):        # getter
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
print(acc.owner)           # Supriya (public - works)
# acc.__balance            # AttributeError!

# Python stores private as: _BankAccount__balance
print(acc._BankAccount__balance)  # 1500 (still accessible this way)
```

### Access Levels

| Prefix | Type | Accessible |
|---|---|---|
| `name` | Public | Anywhere |
| `_name` | Protected | Convention — don't use outside class |
| `__name` | Private | Name mangled — truly hidden |

> **Interview tip:** "In Python, double underscore triggers name mangling — the attribute still exists but can't be accessed directly. It's convention-based, not strictly enforced like Java."

---

## 5. Abstraction

> **Hide implementation details. Show only what's necessary using ABC.**

```python
from abc import ABC, abstractmethod

class BasePage(ABC):   # abstract class — cannot be instantiated
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def navigate(self):    # child MUST implement this
        pass

    @abstractmethod
    def is_loaded(self):   # child MUST implement this
        pass

    def click(self, element):   # shared method — available to all children
        element.click()


class LoginPage(BasePage):
    def navigate(self):
        self.driver.get("/login")

    def is_loaded(self):
        return "login" in self.driver.current_url


# BasePage(driver)   → TypeError: Can't instantiate abstract class
page = LoginPage(driver)  # ✅ works
```

> **Interview tip:** "Abstraction in my framework means `BasePage` defines what every page must have — `navigate()` and `is_loaded()` — but each page implements it differently. This is exactly how Page Object Model works."

---

## 6. Magic Methods (Dunder)

> **Special methods with double underscores that Python calls automatically.**

```python
class TestResult:
    def __init__(self, name, passed):
        self.name = name
        self.passed = passed

    def __str__(self):           # called by print(obj)
        status = "✅" if self.passed else "❌"
        return f"{status} {self.name}"

    def __repr__(self):          # called in debug / REPL
        return f"TestResult(name={self.name}, passed={self.passed})"

    def __eq__(self, other):     # called by == operator
        return self.name == other.name

    def __len__(self):           # called by len(obj)
        return len(self.name)

    def __contains__(self, item):  # called by `in` operator
        return item in self.name


r = TestResult("test_login", True)
print(r)           # ✅ test_login
print(repr(r))     # TestResult(name=test_login, passed=True)
print(len(r))      # 10
print("login" in r)  # True
```

### Quick Reference

| Magic Method | When called |
|---|---|
| `__init__` | Object creation |
| `__str__` | `print(obj)` — user-friendly |
| `__repr__` | `repr(obj)` — debug representation |
| `__len__` | `len(obj)` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__add__` | `obj1 + obj2` |
| `__getitem__` | `obj[key]` |
| `__contains__` | `x in obj` |
| `__enter__` | `with obj:` start |
| `__exit__` | `with obj:` end |

> **Interview tip:** "`__str__` is for end users (print), `__repr__` is for developers (debug). Always define `__repr__` at minimum."

---

## 7. Properties (getter/setter)

> **Control attribute access with `@property` decorator — Pythonic encapsulation.**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private

    @property
    def salary(self):            # getter
        return self.__salary

    @salary.setter
    def salary(self, value):     # setter with validation
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self.__salary = value

    @salary.deleter
    def salary(self):            # deleter
        del self.__salary


emp = Employee("Supriya", 50000)
print(emp.salary)    # 50000 (getter called)
emp.salary = 60000   # setter called — works
emp.salary = -1      # ValueError: Salary cannot be negative!
```

### Why @property over Java-style getters?

```python
# Without @property (Java style — verbose)
emp.set_salary(60000)
emp.get_salary()

# With @property (Pythonic — clean)
emp.salary = 60000   # looks like normal attribute access
emp.salary           # but validation runs underneath
```

> **Interview tip:** "`@property` gives you the clean syntax of direct attribute access while keeping validation logic hidden — best of both encapsulation and usability."

---

## 8. Class method vs Static method

> **`classmethod` gets the class, `staticmethod` gets nothing — just a utility.**

```python
class DateHelper:
    date_format = "%Y-%m-%d"   # class variable

    def __init__(self, date):
        self.date = date

    @classmethod
    def from_string(cls, date_str):
        # cls = DateHelper class itself
        # used as an alternate constructor
        return cls(date_str)

    @staticmethod
    def is_valid(date_str):
        # no self, no cls — pure utility function
        return len(date_str) == 10


# classmethod — alternate constructor
d = DateHelper.from_string("2024-01-15")

# staticmethod — utility, no instance needed
print(DateHelper.is_valid("2024-01-15"))  # True
print(DateHelper.is_valid("24-1-15"))     # False
```

### SDET Use Case

```python
class APIClient:
    @staticmethod
    def build_headers(token):
        # no instance needed — pure utility
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    @classmethod
    def from_config(cls, config):
        # alternate constructor from config file
        return cls(base_url=config["base_url"])
```

### Comparison Table

| | `self` | `cls` | Use case |
|---|---|---|---|
| Instance method | ✅ | ❌ | Normal methods, access instance state |
| `@classmethod` | ❌ | ✅ | Alternate constructors, factory methods |
| `@staticmethod` | ❌ | ❌ | Pure utility — no state needed |

> **Interview tip:** "I use `@staticmethod` for pure utility functions like building headers or validating formats — they don't need instance or class state. `@classmethod` is useful for alternate constructors like loading from a config file."

---

## Quick Summary

| Concept | One-line definition |
|---|---|
| **Class & Object** | Class = blueprint, Object = instance with its own state |
| **Inheritance** | Child reuses and extends parent class behaviour |
| **Polymorphism** | Same method name, different behaviour per class |
| **Encapsulation** | Hide internal data, expose only what's needed |
| **Abstraction** | Define a contract (ABC) without full implementation |
| **Magic Methods** | Special `__dunder__` methods Python calls automatically |
| **Properties** | Pythonic getter/setter with `@property` decorator |
| **Class vs Static** | `@classmethod` gets class, `@staticmethod` gets nothing |

---

*Generated for SDET interview preparation — Python OOP concepts with automation framework context.*
