names = ["Anu", "Ravi", "Esha", "Uday", "Kiran", "Om"]
result = list(filter(lambda x: x[0].lower() in 'aeiou', names))
print(result)