try:
	num1 = int(input("enter num1: "))
	num2 = int(input("enter num2: "))
	
	result = num1 / num2
	
        print("Result:", result)
        
except ZeroDivisionError:
	print("Error")
except ValueError:
	print("Error")
finally:
	print("done")
