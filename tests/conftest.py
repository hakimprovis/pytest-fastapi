def mydecor (func):
    def wrapper (*args, **kwargs):
        print("HAk")
        func(*args, **kwargs)
        print("QA")
    return wrapper
@mydecor
def f (x):
    print("AUTO:" + str(x))

f(5)
