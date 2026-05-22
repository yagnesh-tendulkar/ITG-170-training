 # 10. Filter names longer than 4 letters
names = ["John", "Alexander", "Emma", "Sophia", "Raj"]
long_names = [name for name in names if len(name) > 4]

print("\nNames longer than 4 letters:", long_names)
