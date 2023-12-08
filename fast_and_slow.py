import time

def speed_calc_decorator(function):
    def cal_speed():
        start = time.time()
        function()
        end = time.time()
        time_running = end - start
        print(f"{function.__name__} run speed: {time_running}")

    return cal_speed

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i*i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i*i

fast_function()
slow_function()