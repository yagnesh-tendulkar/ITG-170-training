book_price = float(input("Enter price of the book: "))
quantity = int(input("Enter quantity: "))

total_cost = book_price * quantity

print("\n FINAL BILL")
print(f"Book Price : ₹{book_price}")
print(f"Quantity   : {quantity}")
print(f"Total Cost : ₹{total_cost}")
