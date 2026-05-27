roll_no = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
marks = [85, 98, 89, 92]
result = []
for i in range(len(roll_no)):
    d = {roll_no[i]: {names[i]: marks[i]}}
    result.append(d)
print(result)