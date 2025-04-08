items_total = 0

for i in range(4):
    item_name = input("Enter item name: ")
    item_price = float(input(f"Enter the price of {item_name}: "))
    items_total += item_price
    
amount_paid = float(input("Enter the toatl amount you paid: "))
change = amount_paid - items_total
    
print(f"The total cost of items is R{items_total}")
print(f"You paid R{amount_paid} ")
print(f"Your change is R{change}")

