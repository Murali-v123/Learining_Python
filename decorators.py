def wrappper_fun(func):
    def wrappe(a,b):
        print("------------")
        func(a,b)
        print("------------")
    return wrappe

@wrappper_fun
def add(a,b):
    print(a+b)

add(2,3)

def greet(func):
    def wrapper(name):
        print("Hello!")
        func(name)
        print("Have a nice day!")
    return wrapper

def say_name(name):
    print(f"My name is {name}")

greet(say_name)("Murali")

def logger(func):
    def wrapper():
        print(f"Function '{func.__name__}' is being called.")
        func()
    return wrapper

@logger
def add():
    print("Hey there!")

add()

# Create a function view_data(name)
# Decorator allow_only(name) should print “Access Denied” if the name is not "admin"

def fun(func):
    def check(name):
        if name=="admin":
            func(name)
        else:
            print("Access denied")
    return check

@fun
def view_data(name):
    print(f"access allowed for {name}")

view_data("hello")