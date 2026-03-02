names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

print("Steps Dataset Demo")

print("Jake's steps on Wednesday:", steps[2][2])

steps[1][0] = 4300
print("Updated Lia's steps on Monday:", steps[1][0])

print()

all_steps = []

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    
    print(names[i], "total steps:", total)
    print(names[i], "average steps:", round(average, 2))
    print()
    
    all_steps.extend(steps[i])