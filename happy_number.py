def happy_number(number):

    while number != 1 and number != 4:

        total = 0

        while number != 0:
            rem = number % 10
            total += rem * rem
            number = number // 10

        number = total

    if number == 1:
        print("Happy Number")
    else:
        print("Not a Happy Number")


happy_number(112)