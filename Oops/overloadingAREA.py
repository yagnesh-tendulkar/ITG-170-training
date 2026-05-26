class shape:
    def area(self,a,b=None):
        if b is None:
            print("Area of square : ",a*a)
        else:
            print("Area of rectangle : ",a*b)
sh=shape()
sh.area(10)
sh.area(10,30)