names = ["Analysis", "Ventilation", "Arcturus", "Barcturus", "Carcturus"]

scores = [
    [85, 90, 88],   # Analysis
    [78, 82, 80],   # Ventilation
    [92, 89, 94],   # Arcturus
    [76, 75, 72],   # Barcturus
    [88, 91, 87]    # Carcturus
]

print("Weekly Score Analysis")

totals = []

for i in range(len(scores)):
    total = sum(scores[i])
    totals.append(total)
    print(names[i], "total score:", total)

highest_total = max(totals)
lowest_total = min(totals)

highest_index = totals.index(highest_total)
highest_student = names[highest_index]

print("\nStudent with the highest total score:", highest_student)
print("Highest total score:", highest_total)

difference = highest_total - lowest_total
print("Difference between highest and lowest total:", difference)