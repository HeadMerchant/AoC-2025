from common import dailyPuzzle
from pprint import pprint

file = dailyPuzzle(5)
test = (
"""3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
).splitlines()

# file = test
file = iter(file)
ranges: list[tuple[int, int]] = []

for validRange in file:
    validRange = validRange.strip()
    if not validRange:
        break

    low, high = validRange.split('-')
    ranges.append((int(low), int(high)))

validIds = 0
for foodId in file:
    foodId = int(foodId.strip())
    for low, high in ranges:
        if low <= foodId <= high:
            validIds += 1
            break

ranges.sort()
# print(ranges)
newRanges = [ranges[0]]
for range in ranges:
    low, high = range
    prevLow, prevHigh = newRanges[-1]
    if low <= prevHigh:
        newRanges[-1] = prevLow, max(high, prevHigh)
    else:
        newRanges.append((low, high))

# print(newRanges)
print(validIds, sum(high - low + 1 for low, high in newRanges))
