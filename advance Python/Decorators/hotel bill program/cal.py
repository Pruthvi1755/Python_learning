def calculate(par):
    def wrapper(name, qty):
        par(name,qty)

        if name == 1:
            price = 70
        elif name == 2:
            price = 50
        elif name == 3:
            price = 100
        else:
            print("invalid no")

        total = price*qty
        print(f'Rs {total}')

    return  wrapper