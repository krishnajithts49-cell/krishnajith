class Ticket:
    def__init__(self,name,base_price):
        self.name= name
        self.base_price=base_price

        def price(self):
            return self.base_price



concert=Ticket("concert",200)
museum=Ticket("Muesum",150)
print(concert.name,concert.price())
print(museum.name,museum.price())
