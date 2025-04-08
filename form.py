total_fruit = 0
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in week_days:
    fruit = int(input(f"Enter pieces of fruit you ate on {day}: "))
    total_fruit += fruit
    print(f"On {day}, you ate {fruit} pieces of fruit.")
print(f"\nTotal fruit eaten this week: {total_fruit}")

print()

items_total = 0

for i in range(4):
    item_name = input("Enter item name: ")
    item_price = float(input(f"Enter the price of {item_name}: "))
    amount_paid = float(input("Enter amount paid: "))
    change = amount_paid - items_total
    items_total += item_price
print(f"\nThe total cost of selected items is R{items_total} and your change is R{change}")

