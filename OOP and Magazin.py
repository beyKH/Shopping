import time

class Seller():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def sell_product(self):
        product_id = input("please enter id of the product: ")
        for product_temp in prodcut_list:
            if product_temp.id == product_id:
                print("""
                        ID: {}
                        Name: {}
                        Price: {}
                          """.format(product_temp.id, product_temp.name, product_temp.price))
                print("you")
                answer = input("do you want to sell it? (y/n)")
                if answer == "y":
                    prodcut_sold_list.append(product_temp)
                    prodcut_list.remove(product_temp)

    def show_available_products(self):
        print(" It is all prodcut list")
        if len(prodcut_list) >= 1:
            for product_temp in prodcut_list:
                print("""

                           ID : {}
                           Name: {}
                           Price : {}

                           """.format(product_temp.id, product_temp.name, product_temp.price))
        else:
            print("no products available")

    def show_sold_products(self):

        if len(prodcut_sold_list) >= 1:
            print(" It is all prodcut list")
            for product_temp in prodcut_sold_list:
                print("""
            
                        ID : {}
                        Name: {}
                        Price : {}
            
                        """.format(product_temp.id, product_temp.name, product_temp.price))
        else:
            print("no products")


class Product():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


prodcut_list = []
prodcut_sold_list = []
seller = Seller('1', "1")

p1 = Product(1, "apple", 2000)
prodcut_list.append(p1)

stop = False
while stop != True:

    login = input("please enter login : ")
    password = input("please enter password: ")
    if seller.login == '1' and seller.password == '1':
        while stop != True:

            print("You entered account succesfully")

            print("""
                            1. Add Product 
                            2. Sell Prodcut
                            3. Available Product
                            4. Sold Product
                            5. Exit 
                            """)
            choice = int(input("please enter choice : "))

            if choice == 2:
                seller.sell_product()
                time.sleep(2)
            elif choice == 3:
                seller.show_available_products()
                time.sleep(2)

            elif choice == 3:
                seller.show_sold_products()
                time.sleep(2)
