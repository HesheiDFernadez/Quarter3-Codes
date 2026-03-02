names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

print("Highest Total Steps (Per Person)")

totals = []

for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(names[i], "total steps:", total)

highest_total = max(totals)
lowest_total = min(totals)

highest_index = totals.index(highest_total)
highest_person = names[highest_index]

print("\nPerson with highest total steps:", highest_person)
print("Highest total:", highest_total)
print("Difference between highest and lowest:", highest_total - lowest_total)