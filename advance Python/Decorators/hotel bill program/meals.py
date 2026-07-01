from cal import calculate

@calculate
def meals(name, price, qty):
    print("final bill : ")

n = input(" enter the meal name: ")
p = int(input(" price: "))
q = int(input("qty: "))

meals(n, p, q)
