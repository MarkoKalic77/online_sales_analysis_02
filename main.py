from product import Product
from product_manager import ProductManager
from cart import Cart

pro_menager1=ProductManager()
sto=Product("sto",200,5)
stolica=Product("stolica",50,20)
krevet=Product("krevet",300,4)

pro_menager1.dodavanje(sto)
pro_menager1.dodavanje(stolica)
pro_menager1.dodavanje(krevet)


pro_menager1.popis()
pro_menager1.ukupna_vrednost()

cart1=Cart()
izabrani_sto=Product("sto",200,1)
izabrana_stolica=Product("stolica",50,4)
izabrani_krevet=Product("krevet",300,1)
cart1.dodavanje(izabrani_sto)
cart1.dodavanje(izabrana_stolica)
cart1.dodavanje(izabrani_krevet)
cart1.popis()
cart1.ukupna_vrednost()