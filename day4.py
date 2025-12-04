from common import dailyPuzzle
from pprint import pprint

file = list(line.strip() for line in dailyPuzzle(4))
test = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

file = test
accessible = 0

def neighbors(r: int, c: int):
    for R in range(r-1, r+2):
        for C in range(c-1, c+2):
            if R == r and C == c:
                continue

            if R < 0 or R >= len(file) or C < 0 or C >= len(row):
                continue

            yield R, C
    
q: list[tuple[int, int]] = []
seen: set[tuple[int, int]] = set()
occupiedNeighbors: dict[tuple[int, int], int] = {}

for r, row in enumerate(file):
    for c, char in enumerate(row):
        if char == ".":
            continue

        occupied = 0
        for R, C in neighbors(r, c):
            if file[R][C] == '@':
                occupied += 1

        if occupied < 4:
            accessible += 1
            q.append((r, c))
        occupiedNeighbors[(r, c)] = occupied

fullyAccessible = 0
while q:
    coord = q.pop()
    if coord in seen: continue
    seen.add(coord)
    del occupiedNeighbors[coord]
    fullyAccessible += 1
    for coord in neighbors(*coord):
        if coord in occupiedNeighbors:
            occupiedNeighbors[coord] -= 1
            if occupiedNeighbors[coord] < 4:
                q.append(coord)

print(accessible, fullyAccessible)
