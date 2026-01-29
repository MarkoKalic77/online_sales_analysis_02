class Product:
    def __init__(self, name, price, quantity ):
        self.name=name
        self.price=price
        self.quantity=quantity
    def informacij(self):
        print(f"Product: ime- {self.name}, cena- {self.price}, kolicina- {self.quantity}")
    def azuriranje (self, new_quantity):
        self.quantity=new_quantity