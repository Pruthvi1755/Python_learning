def calculate(par):
    def wrapper(price, qty):
        par(price,qty)

        total = price*qty
        print("Rs", total)

    return  wrapper()