class cal:
    def add (self,*num):
        total=0
        for i in num:
            total+=i
        print("Sum : ",total)
c=cal()
c.add(12,23,34)
c.add(12,4)