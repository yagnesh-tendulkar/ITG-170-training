# lis = [1,2,3,45]
# i = iter(lis)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# custom iterator

class Current:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
c = Current(5)
for i in c:
    print(i)
