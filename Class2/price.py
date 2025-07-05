discount=0

def calculate_tax(price):
    tax = price * 0.08
    return tax

def apply_discount(price, discount):
    discount_amount = price * (discount / 100)
    return discount_amount

price=float(input("Enter the price of the item: "))
tax=calculate_tax(price)
# price 0-99 - no discount, 100-199 - 10% discount, 200-299 - 20% discount, 300+ - 30% discount
if price >= 100 and price < 200: 
    x=apply_discount(price, 10)
elif price >=200:
    x=apply_discount(price, 20)
elif price < 100:
    x=apply_discount(price, 0)

total_price = price - x + tax

print(total_price)
     