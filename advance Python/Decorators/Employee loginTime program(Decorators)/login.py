from datetime import datetime
def login_time(param):
    def inner_function():
        param()
        print(param.__name__(), datetime.today)
    return inner_function