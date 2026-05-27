lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
result = sorted(lst, key=lambda x: x[1])
print(result)