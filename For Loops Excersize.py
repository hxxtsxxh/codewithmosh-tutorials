prices = [
    10,
    15,
    20,
    30,
    35,
    50
]

price = 0

for amount in prices:
    price += amount

tax = float(price) * 0.07
total_price = tax + price
    
print(f"Total without tax: {float(price)}")
print(f"Total with tax: {total_price}")
