class Addition:

    def add(self, a=None, b=None, c=None):

        if a is not None and b is not None and c is not None:
            print("Sum =", a + b + c)

        elif a is not None and b is not None:
            print("Sum =", a + b)

        else:
            print("Provide at least two numbers")

obj = Addition()

obj.add(10, 20, 30)
