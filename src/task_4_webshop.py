#Product
class Product:
    def __init__(self, product_id="0", name=None, price=0):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
    def get_price(self):
        return self.__price
    def __repr__(self):
        return(f" product_name: {self.__name} product_id: {self.__product_id} price: {self.__price}kr")

#ShoppingCart
class ShoppingCart:
    def __init__(self, shoppingcart_id=0):
        self.__shoppingcart_id = shoppingcart_id
        self.__product_list = []
    def add_to_cart(self, product):
        self.__product_list.append(product)
    def remove_from_cart(self, product):
        self.__product_list.remove(product)
    def get_total_price(self):
        total_price = 0
        for product in self.__product_list:
            total_price += product.get_price()
        return total_price
    def get_list_of_items(self):
        return self.__product_list
    def __repr__(self):
        return (f"cart_id: {self.__shoppingcart_id} product_list: {self.__product_list} total_price: ")

#Order
class Order:
    def __init__(self, shopping_list, total_price, order_id=0):
        self.__shopping_list = shopping_list
        self.__total_price = total_price
        self.__order_id = order_id
    def __repr__(self):
        return (f"order_id: {self.__order_id} \nshopping_list: {self.__shopping_list} \ntotal_price: {self.__total_price}")


#skapar en order
#flower = Product(1, "mjöl", 10)
#soap = Product(2, "tvål", 20)
#milk = Product(3, "mjölk", 15)

#cart1 = ShoppingCart()
#cart1.add_to_cart(flower)
#cart1.add_to_cart(soap)
#cart1.add_to_cart(milk)

#price1 = cart1.get_total_price()
#shoppinglist1 = cart1.get_list_of_items()


#order1 = Order(shoppinglist1, price1)
#print(soap)
#print(cart1)
#print(order1)