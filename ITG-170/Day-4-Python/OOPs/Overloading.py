class Arithmatic:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


a = Arithmatic()

print(a.add(1, 2, 3, 4))
print(a.add(1, 2, 3))
print(a.add(1, 2))