names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

print("Weekly Step Summary")

all_steps = []

for i in range(len(steps)):
    print(names[i], "daily steps:", steps[i])
    
    total = sum(steps[i])
    average = total / len(steps[i])
    
    print("  Total:", total)
    print("  Average:", round(average, 2))
    print()
    
    all_steps.extend(steps[i])

print("Highest single-day steps:", max(all_steps))
print("Lowest single-day steps:", min(all_steps))