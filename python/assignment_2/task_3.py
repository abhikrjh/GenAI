orders = []

while True:
    print("\nMenu")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")
    
    choice = input("Enter the choice : ")
    
    if choice == "q":
        print("Existing the program")
        break
    elif choice == "1":
        
        try:
            
            order_amount = float(input("Enter order amount : "))
            orders.append(order_amount)
            print("Order added ", order_amount)
            
        except ValueError:
            print("Invalid amount entered")
            continue
    elif choice == "2":
        if len(orders) == 0:
            print("No order available")
            continue
        
        total_revenue = 0
        
        for order_amount in orders:
            try:
                if order_amount >= 2000:
                    discount = 0.15
                elif order_amount >= 1500:
                    discount = 0.10
                elif order_amount >= 1000:
                    discount = 0.07
                else:
                    discount = 0
                    
                final_amount = order_amount - order_amount * discount
                
                total_revenue += final_amount
                
                print(order_amount, " -> ", discount*100 , "%, -> ", final_amount )
            except ValueError:
                print("Exception while calculating final amount")
        print("Total Revenue : ",total_revenue)
    else:
        print("Invalid input")
        continue
        
        
        
        