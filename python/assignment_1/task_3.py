price_dict = {
    "Laptop":50000,
    "Mobile":20000,
    "Headphones":5000,
    "Keyboard":1000,
    "Mouse":500,
    "Monitor":10000
}

print(price_dict)

#Add
price_dict["Charger"] = 1500
print(price_dict)

#Update
price_dict["Keyboard"] = 1100
print(price_dict)

#average price
total_price = sum(price_dict.values())
total_length = len(price_dict)
avg_price = total_price/total_length

print(f"Average price of price_dict is :", avg_price)
 
 
max_price = list(price_dict.values())[0]
min_price = list(price_dict.values())[0]

for key,value in price_dict.items():
    if max_price < value:
        max_price = value
        
    if min_price > value:
        min_price = value
        
print("Max price : ", max_price)
print("Min price : ", min_price) 
