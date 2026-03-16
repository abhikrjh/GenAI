orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0


for order_amount in orders:
    try:
        if order_amount >= 2000:
            final_amount = order_amount - order_amount * 0.15
            print(order_amount, " -> ", 15, "% -> ", final_amount)
            
        elif order_amount >= 1500:
            final_amount = order_amount - order_amount * 0.10
            print(order_amount, " -> ", 10, "% -> ", final_amount)
            
        elif order_amount >= 1000:
            final_amount = order_amount - order_amount * 0.07
            print(order_amount, " -> ", 7, "% -> ", final_amount)
            
        else:
            final_amount = order_amount
            print(order_amount, " -> ", 0, "% -> ", order_amount)

        total_revenue += final_amount
        
    except ValueError:
        print("Exception while calculating final_amount")
        
    print("Total revenue", total_revenue)

    