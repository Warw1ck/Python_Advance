data = input()
counts = {}

for ch in data:
    if ch not in counts:
        counts[ch] = [0]
    counts[ch][0] += 1

for key in sorted(counts):
    print(f"{key}: {''.join(map(str, counts[key]))} time/s")
