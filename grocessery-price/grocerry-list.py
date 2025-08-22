shopping = []

n = int(input("Enter number of products to add: "))
for i in range(n):
    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    if price > 50:
        discount = price * 0.1
        price -= discount
    else:
        price += 10
    shopping.append({"Product": product, 
                     "Price": price, 
                     "Quantity": quantity})
    
print(shopping)