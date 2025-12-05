from common import dailyPuzzle
from pprint import pprint

file = dailyPuzzle(3)
test = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

file = test

maxJoltage = 0
max12 = 0

def debug():
    print(bank)
    for i, row in enumerate(table):
        if i == 0: continue
        for x in row:
            print(f"{x:{' '}<12}", end = " ")
        print()

j = 0
for bank in file:
    digits = [int(x) for x in bank.strip()]
    n = len(digits)
    tens = max(range(n - 1), key=lambda x: digits[x])
    ones = max(digits[tens+1:])
    
    maxJoltage += digits[tens]*10 + ones

    table = [list(digits) for _ in range(12)]

    place = 10
    for digitPlace in range(1, 12):
        for i in reversed(range(n-digitPlace)):
            current = table[digitPlace][i]
            table[digitPlace][i] = max(table[digitPlace][i+1], current*place + table[digitPlace-1][i+1])
        place *= 10

    biggest = table[-1][0]
    max12 += biggest
    
print(maxJoltage, max12)
