items=['milk','bread','eggs','cheese']
prices=[25,15,30,40]
total_bill=0
items_bought = int(input("how many items did you bought:"))
for i in range(items_bought):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    if item in items:
        index = items.index(item)
        amount = prices[items.index(item)]*quantity
        print(f"The price of {quantity} {item} is {amount}")
    else:
        print(f"{item} is not available")
    total_bill+=amount
    discount=0
    if total_bill > 500:
        discount= total_bill * 0.1
        total_bill -= discount
    else:
        total_bill += discount
    if total_bill > 1000:
        discount = total_bill * 0.2
        total_bill -= discount
    else:
        total_bill += discount
print(f"Your total bill is {total_bill}")
