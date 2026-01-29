from product import Product
from product_manager import ProductManager

pro_menager1=ProductManager()
sto=Product("sto",200,5)
stolica=Product("stolica",50,20)
krevet=Product("krevet",300,4)

pro_menager1.dodavanje(sto)
pro_menager1.dodavanje(stolica)
pro_menager1.dodavanje(krevet)


pro_menager1.popis()
pro_menager1.ukupna_vrednost()