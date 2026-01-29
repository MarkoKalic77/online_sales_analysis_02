class ProductManager:
    products=[]
    def dodavanje (self, new_product):
        self.products.append(new_product)
    def popis(self):
        for i in self.products:
            print(f"{i.name}")
    def ukupna_vrednost (self):
        suma=0
        for i in self.products:
            suma+=i.price*i.quantity
        print(f"{suma}")
    def uklanjanje_proizvoda(self,ime):
        self.products.remove(ime)