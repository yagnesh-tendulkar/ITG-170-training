class My(Exception):
    try:
        num1=int(input("enter number : "))
        print(f"Numbeer Entered is {num1}")
        
    except ValueError as e:
        print(f"Message {e}")