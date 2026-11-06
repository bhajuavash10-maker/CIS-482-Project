import random

diameter = [60, 120, 180, 240]
distance = [100, 200, 300, 400]
direction = ["L", "R"]
results = []
for d in diameter:
    for dist in distance:
        for dir in direction:
            result = f"[{d}, {dist}, {dir}]"
            results.append(result)

random.shuffle(results)
print(results)
