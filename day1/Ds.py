#data structures functions and sorting


students = {
    "Arika": [85, 90, 88],
    "Rahul": [70, 75, 80],
    "Sneha": [92, 95, 91]
}


def calculate_average(marks):
    return sum(marks) / len(marks)


averages = {
    name: calculate_average(scores)
    for name, scores in students.items()
}

# Sort students by average marks
sorted_students = sorted(
    averages.items(),
    
    key=lambda x: x[1],
    reverse=True
)

for name, avg in sorted_students:
    print(f"{name}: {avg:.2f}")
