class Product:
    def __init__(self, ID, name, quantity, price):
        self.ID = ID
        self.name = name
        self.quantity = quantity 
        self.price = price
    
    def setProductID(self,x):
        self.ID = x
    def setProductname(self,x):
        self.name = x
    def setProductquantity(self,x):
        self.quantity = x
    def setProductprice(self,x):
        self.price = x
        
    def getID(self):
        return self.ID
    def getname(self):
        return self.name
    def getquantity(self):
        return self.quantity
    def getprice(self):
        return self.price
   
    def myfunc(self):
        print('(' + str(self.ID) + ') ' + str(self.name) + ' $ ' + str(self.price))
    
    
    

Product_list = []
Product_list.append(Product(0, "Ultrasonic range finder", 4, 2.50))
Product_list.append(Product(1, "Servo motor", 10, 14.99))
Product_list.append(Product(2, "Servo Controller", 5, 44.95))
Product_list.append(Product(3, "Microcontroller Board", 7, 34.95))
Product_list.append(Product(4, "Laser range finder", 2, 149.99))
Product_list.append(Product(5, "Lithium polymer battery", 8, 8.99))
    
    


def print_stock():
    print("\nAvailable Products")
    print("---------------")
    for i in range(0,6):
        Product_list[i].myfunc()
    print()
        



def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter Product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])
        
        if Product_list[prod_id].getProductquantity() >= count:
            if cash >= Product_list[prod_id].getProductcost():
                Product_list[prod_id].getProductquantity() * count
                cost = Product_list[prod_id].getProductcost() * count
                cash -= cost
                print("You purchased", count, Product_list[prod_id].getProductname() + " for $" + str(cost) + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
                Product_list[prod_id].setProductquantity(Product_list[prod_id].getProductquantity() - count)
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we do not have that many", Product_list[prod_id].getProductname())
        


main()