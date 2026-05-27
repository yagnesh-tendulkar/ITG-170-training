#Prints 1 to N numbers using recursion 

def print_numbers(number, end_number):
    if number <= end_number:
        print(number, end=" ")
        print_numbers(number+1, end_number)

start_number = 1 
end_number = int(input("Enter end number: "))
print_numbers(start_number, end_number)