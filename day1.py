from common import dailyPuzzle

file = dailyPuzzle(1)
# file = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82"
# ]

file = [
    "R1000"
]

position = 50
zeroStops = 0
zeroPasses = 0
dialLength = 100
for line in file:
    direction = -1 if line[0] == 'L' else 1
    rotate = int(line[1:])
    startedZero = position == 0
    if direction > 0:
        targetAmount = dialLength - position
    else:
        targetAmount = position

    position += direction * rotate

    rotate -= targetAmount
    if rotate >= 0:
        zeroPasses += rotate // dialLength
        zeroPasses += int(not startedZero)

    position %= dialLength
    if position == 0:
        zeroStops += 1
print(zeroStops, zeroPasses)
