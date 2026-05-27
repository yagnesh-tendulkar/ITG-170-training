#pattern 1
def pattern1():
    no_of_rows = int(input())
    spaces = no_of_rows-1
    no_of_stars=1
    for i in range(no_of_rows):
        print(spaces*" "+"* "*no_of_stars)
        spaces-=1
        no_of_stars+=1
        
# Pattern 2
def pattern2():
    no_of_rows = int(input())

    spaces = no_of_rows - 1
    no_of_stars = 1

    for i in range(no_of_rows):
        print(spaces * " " + no_of_stars * "*")
        spaces -= 1
        no_of_stars += 2


    spaces = 1
    no_of_stars -= 4

    for i in range(no_of_rows - 1):
        print(spaces * " " + no_of_stars * "*")
        spaces += 1
        no_of_stars -= 2


# Pattern 3
def pattern3():
    no_of_rows = int(input())

    spaces = 0
    no_of_stars = no_of_rows

    for i in range(no_of_rows):
        print(spaces * " " + "* " * no_of_stars)
        spaces += 1
        no_of_stars -= 1

# Pattern 4
def pattern4():
    no_of_rows = int(input())
    for i in range(1,no_of_rows):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    

# Pattern 5
def pattern5():
    no_of_rows = int(input())
    number=1
    for i in range(1,no_of_rows):
        for j in range(1,i+1):
            print(number, end=" ")
            number+=1
        print()  

# Pattern 6
def pattern6():
    no_of_rows = int(input())
    for i in range(1,no_of_rows+1):
        for j in range(no_of_rows,no_of_rows-i,-1):
            print(j,end=" ")
        print()    

# Pattern 7
def pattern7():
    no_of_rows = int(input())
    for i in range(1,no_of_rows+1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print() 

# Pattern 8
def pattern8():
    no_of_rows = int(input())
    for i in range(1,no_of_rows+1):
        idx=1
        for j in range(i,0,-1):
            print(idx,end="")
            idx=1-idx
        print() 

# Pattern 9
def pattern9():
    no_of_rows = int(input())
    spaces=no_of_rows-1
    prev="1"
    print(" "*spaces+prev)
    spaces-=1
    for i in range(2,no_of_rows+1):
        cur=str(i)+prev+str(i)
        print((" "*spaces)+(cur)) 
        prev=cur
        spaces-=1

# Pattern 10
def pattern10():
    n = int(input())
    spaces=0
    # upper part
    for i in range(1, n + 1):
        print((spaces*" "),end="")
        for j in range(i, n + 1):
            print(str(j), end=" ")
        spaces+=1
        print()
    spaces=n-2
    # lower part
    for i in range(n - 1, 0, -1):
        print((spaces*" "),end="")
        for j in range(i, n + 1):
            print(j, end=" ")
        spaces-=1    
        print() 

# Pattern 11
def pattern11():
    n = int(input())

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")

            if j != i:
                print("*", end="")
        print()

# Pattern 12
def pattern12():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()

# Pattern 13
def pattern13():
    n = int(input())
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()

# Pattern 14
def pattern14():
    n = int(input())
    for i in range(1, n + 1):
        print("*" * (i - 1) + str(i) + "*" * (i - 1))

# Pattern 15
def pattern15():
    n = int(input())
    for i in range(1, n + 1):
        print("*" * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        print()

choice = int(input("Enter pattern number (1-15): "))

if choice == 1:
    pattern1()

elif choice == 2:
    pattern2()

elif choice == 3:
    pattern3()

elif choice == 4:
    pattern4()

elif choice == 5:
    pattern5()

elif choice == 6:
    pattern6()

elif choice == 7:
    pattern7()

elif choice == 8:
    pattern8()

elif choice == 9:
    pattern9()

elif choice == 10:
    pattern10()

elif choice == 11:
    pattern11()

elif choice == 12:
    pattern12()

elif choice == 13:
    pattern13()

elif choice == 14:
    pattern14()

elif choice == 15:
    pattern15()

else:
    print("Invalid Pattern Number")