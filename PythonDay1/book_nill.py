def Book_bill(total_cost):
    print(f"The final bill to pay is {total_cost} $ only /- ")

price_of_book = int(input("Enter the price of the book : "))
Quantity = int(input("Enter the Quantity of the book : "))
total_cost = price_of_book * Quantity
Book_bill(total_cost)