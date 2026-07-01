from cal import calculate

@calculate
def meals(name, qty):
    print("final bill : ")

n = int(input("items \n 1.dosa,\n 2. idle,\n 3.poliogre \nenter the meal no:"))

q = int(input("qty: "))

meals(n, q)
