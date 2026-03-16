daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily_sales:
    
    if sale == -1:
        print("Corrupted data")
        break
    elif sale == 0:
        print("Day with no sales")
        continue
    else:
        total_sales += sale
        print("Running total : ", total_sales)
        

print("final total ", total_sales)