scores = [
    [85, 90, 88],   # Analysis
    [78, 82, 80],   # Ventilation
    [92, 89, 94],   # Arcturus
    [76, 75, 72],   # Barcturus (w updated Math score)
    [88, 91, 87]    # Carcturus
]

students = ["Analysis", "Ventilation", "Arcturus", "Barcturus", "Carcturus"]

print("Weekly Test Scores Summary:")

for i in range(len(scores)):
    print(students[i], "scores:", scores[i])
    
    total = sum(scores[i])
    average = total / len(scores[i])
    
    print("  Total:", total)
    print("  Average:", round(average, 2))
    print()

all_scores = []
for row in scores:
    all_scores.extend(row)

print("Highest score in dataset:", max(all_scores))
print("Lowest score in dataset:", min(all_scores))