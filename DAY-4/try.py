try:
    # This will cause ValueError
    x = int(input("Enter a number:")) 
    inv = 1 / x   # Inverse calculation
    
except Exception as e:
    print("Not Valid!", e)