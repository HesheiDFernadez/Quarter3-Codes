# weekly test scores

# rows = students, columns = subjects
scores = [
    [85, 90, 88],   # Analysis
    [78, 82, 80],   # Ventilation
    [92, 89, 94],   # Arcturus
    [70, 75, 72],   # Barcturus
    [88, 91, 87]    # Carcturus
]

students = ["Analysis", "Ventilation", "Arcturus", "Barcturus", "Carcturus"]
subjects = ["Math", "Science", "English"]

# access a specific value
print("Arcturus's English score:", scores[2][2])

# update a specific value
scores[3][0] = 76
print("Barcturus's updated Math score:", scores[3][0])

# summarize data
analysis_average = sum(scores[0]) / len(scores[0])
print("Analysis's average score:", analysis_average)

# calculate overall class average
total = 0
count = 0
for row in scores:
    total += sum(row)
    count += len(row)

class_average = total / count
print("Class average:", class_average)