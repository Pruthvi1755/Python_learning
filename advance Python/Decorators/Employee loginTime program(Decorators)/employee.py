from login import login_time

@login_time
def employee1():
    print("login time")

@login_time
def employee2():
    print()

employee1()
employee2()

