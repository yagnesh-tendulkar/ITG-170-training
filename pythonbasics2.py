#small introduction paragraph using multi line


s="""hi everyone this is vaishnavi working as a software trainee
    for miracle software systems"""
print(s)

#create variable for price book,quantity,cost
book_price=int(input("enter book price: "))
quantity=int(input("enter quantity: "))
print(f"the total cost is:  {book_price*quantity}")



#age calc using yob
birth_year=int(input("enter your birth year: "))
print(2026-birth_year)



#TAKE NAME AND PRINT LOWER CASE UPPER AND LEN OF NAME
name=input("Enter your name: ")
print(name.upper(),name.lower(),len(name),sep="\n")



#ask user to enter temp convert celsius to farrenheit
cel=int(input("enter celsius temp"))
print(((9/5)*cel)+32,"f")