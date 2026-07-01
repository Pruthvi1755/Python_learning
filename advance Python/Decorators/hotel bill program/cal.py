def calculate(par):
    def wrapper(name, price, qty):
        par(name, price,qty)

        total = price*qty
        print(f'{name} --> Rs {total}')

    return  wrapper()