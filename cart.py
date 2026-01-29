class Cart:
    cart_items=[]
    def dodavanje (self, new_product):
        self.cart_items.append(new_product)
    def ukupna_vrednost (self):
        suma=0
        for i in self.cart_items:
            suma+=i.price*i.quantity
        print(f"{suma}")
    def popis(self):
        for i in self.cart_items:
            print(f"{i.name}")