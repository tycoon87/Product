class Product(object):
    def __init__(self,price,item_name,waight,brand,cost,stats):
        self.price = price
        self.item_name = item_name
        self.waight = waight
        self.brand = brand
        self.cost = cost
        self.stats = "for sale"
        self.tax = 0.15
        
    def sell(self):
        self.stats = "sold"
        print "this item is {}".format(self.stats)
        return self
        
    def add_tax(self):
        temp = self.price * self.tax
        self.price = self.price + temp
        print "price: ${}" .format(self.price)
        return self
    
    def returned(self):
        if (self.stats == "defective"):
            self.stats = "defective"
            self.item_price = 0
        elif(self.stats == "like new"):
            self.stats = "for sale"
        elif(self.stats == "opened"):
            self.stats = "opened"
            temp = self.price * 0.20
            self.price = self.price - temp
            print "this product is {} and is ${}".format(self.stats,self.price)
            return self
        
item1 = Product(20, "thing1", 5, "jonson&jonson", 7, "for sale")
item2 = Product(13, "thing2", 2, "brand 2", 5, "defective")
item3 = Product(40, "thing3", 8, "brand 3", 13, "opened")
item1.add_tax()
item1.sell()
item2.returned()
item3.returned()
