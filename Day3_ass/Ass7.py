"""Create a dictionary of a product: name, price, quantity
Calculate total cost."""
product={
    "Name":"TV",
    "Price":40000,
    "Quantity":4
}
total_cost=product["Price"]*product["Quantity"]
print("Total cost of all products:",total_cost)