from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        function()
    
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()