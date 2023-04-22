# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
# if __name__ == '__main__':
#     app.run()


# from time import sleep
#
#
# def my_decorator(function):
#     def my_wrapper():
#         sleep(2)
#         function()
#
#     return my_wrapper
#
# @my_decorator
# def yo():
#     print("YO")
#
# def oi():
#     print("OI")
#
# delay = my_decorator(oi)
# delay()
#
# yo()


import time

def speed_calc_decorator(function):
    def wrapper():
        time_start = time.time()
        function()
        time_end = time.time()
        print(f"{function.__name__} runspeed: {time_end - time_start}")

    return wrapper

@speed_calc_decorator
def fast_function():
    time.sleep(1)

@speed_calc_decorator
def slow_function():
    time.sleep(5)

fast_function()
slow_function()