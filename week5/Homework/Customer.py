import Productcheck as prod

def buy(product, num, price):
    if prod.check(product, num) == True:
        print("You bought " + product + " and spent ", num * price)
    else:
        print("Sorry! We are out of this product.")

def main():
    return buy('pen', 5, 10)

if __name__ == '__main__':
    main()
