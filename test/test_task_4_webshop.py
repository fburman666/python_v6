from src.task_4_webshop import *

#testdata från chatgpt:
#Tabellen innehåller produktens namn, pris och ett unikt ID för varje produkt:
#ID	    Namn	    Pris (SEK)
#A1B2C3	Skruvmejsel	199
#D4E5F6	Borrmaskin	999
#G7H8I9	Hammare	    159
#J1K2L3	Tång	    349
#M4N5O6	Kapsåg	    1299
#P7Q8R9	Slipmaskin	799
#S1T2U3	Rörtång	    699
#V4W5X6	Spikpistol	2499
#Y7Z8A9	Måttband	159
#B1C2D3	Vattenpump	899

product1 = Product("A1B2C3", "Skruvmejsel", 199)
product2 = Product("D4E5F6", "Borrmaskin", 999)
product3 = Product("G7H8I9", "Hammare", 159)
cart1 = ShoppingCart()
cart1.add_to_cart(product1)
cart1.add_to_cart(product2)
cart1.add_to_cart(product3)

#verifiera att totala priset blir rätt
assert cart1.get_total_price() == 1357