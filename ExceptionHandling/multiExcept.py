try:
    num1=int(input("Enter a Number"))
    num2=int(input("Enter a Number"))

    result=num1/num2
    print("Result : ",result)

    my_list=[1,2,3]
    my_list[3]=45
    print(f"forth element : {my_list[4]}")


except ZeroDivisionError:
    print("Error : Enter a non negative Integer")

except ValueError:
    print("Error: Enter a valid Value")

except IndexError:
    print("Error : index out of bound ")

except Exception as e:
    print(f"Exception : {e}")

finally:
    print("This finally block executes always")