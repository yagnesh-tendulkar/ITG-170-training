# iterators 
# Create iterator for even numbers till N
# n = 10
class Eve:
    def __init__(self,n):
        self.n = n
        self.even_num =1
    def __iter__(self):
        return self
    def __next__(self):
        while self.even_num <= self.n:
            if self.even_num % 2 == 0:
                val = self.even_num
                self.even_num += 1
                return val
            self.even_num += 1
        
        raise StopIteration
e = Eve(10)
for i in e:
    print(i)
        


