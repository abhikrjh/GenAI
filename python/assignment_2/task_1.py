order_amount = int(input("Enter amount : "))

discount = 0

if order_amount >= 2000:
    discount = 0.15
elif order_amount >= 1500:
    discount = 0.10
elif order_amount >= 1000:
    discount = 0.07
else:
    discount = 0

order_amount = order_amount - order_amount * discount
print("order_amount", order_amount)
