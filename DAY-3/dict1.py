# #Create a dictionary storing:
# Name
# Age
# Course
# Print all keys and values.
details={"name":"John Doe","age":22,"course":"ITG"}
print(details.items())#prints key-value pairs of the dictionary in the form of tuples
print(details.keys())#prints keys of the dictionary
print(details.values())#prints values of the dictionary
print(details)#prints the whole dictionary


#Create a dictionary comprehension to store squares of numbers from 1–5.
square={i: i*i for i in range(1,6)}
print(square)
print()

# Create a dictionary of a product: name, price, quantity
# Calculate total cost.
print()
product={"name":"iphone","price":200000,"quanity":2}
tota_cost=product["price"]*product["quanity"]
print(f"Total cost of {product['name']} is {tota_cost}")