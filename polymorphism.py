class Test:
   
    def add(*args):
        sum=1
        for i in args:
            sum=sum*i

        print(sum) 
        print("method overloading")
class Demo(Test):
    def add(*args):
        sum=0
        for i in args:
            sum=sum+i
        print(sum)
        print("method over_riding")
              
Test.add(2,3,5) 
Test.add(2,3) 
Demo.add(2,3)             