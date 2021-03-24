class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.price = price
        self.name = name


p1 = Product(1, "olma", 200)
p2 = Product(2, "olma", 300)
product_list = [p1, p2]
sold_product_list = []


class Seller():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def sell_product(self):
        for product in product_list:
            print("""
                        ID: {}
                        NAME : {}
                        PRICE: {}
                        """.format(product.id, product.name, product.price))

        id = int(input("please enter id"))

        for i in product_list:
            if i.id == id:
                print("successfully sold")
                sold_product_list.append(i)
                product_list.remove(i)

    def available_product(self):

        if len(product_list) > 0:
            for product in product_list:
                print("""   
                ID: {}
                NAME : {}
                PRICE: {}
                 """.format(product.id, product.name, product.price))
        else:
            print("Sorry no products now")

    def add_products(self):
        isrepeated = True
        id = int(input("please enter id: "))
        name = input("please enter name: ")
        price = int(input("please enter price: "))

        product = Product(id, name, price)
        product_list.append(product)

    def sold_proucts(self):
        if len(sold_product_list) > 0:
            for product in sold_product_list:
                print("""
                        ID: {}
                        NAME : {}
                        PRICE: {}
                """.format(product.id, product.name, product.price))

        else:
            print("There is no availabe sold products")


seller = Seller("1", "1")

stop = False
while stop != True:

    login = input("please enter login : ")
    password = input("please enter password: ")
    if seller.login == login and seller.password == password:
        print("You entered account succesfully")
        while stop != True:

            print("""
                            1. Sell 
                            2. Available
                            3. Sold Products
                            4. Add Product
                            """)
            choice = int(input("please enter choice : "))

            if choice == 1:
                seller.sell_product()
            elif choice == 2:
                seller.available_product()
            elif choice == 3:
                seller.sold_proucts()
            elif choice == 4:
                seller.add_products()
