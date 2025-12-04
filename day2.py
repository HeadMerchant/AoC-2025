from common import dailyPuzzle

file = dailyPuzzle(2).readline()
# file = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

invalid1 = 0
invalid2 = 0

for nums in file.split(","):
    A, B = nums.split("-")
    a = int(A)
    b = int(B)

    for x in range(a, b+1):
        num = str(x)
        n = len(num)
        if n % 2 == 0 and num[:n//2] == num[n//2:]:
            invalid1 += int(num)
        
        for length in range(1, n//2 + 1):
            testSequence = num[:length]
            seqs = (num[start:start+length] == testSequence for start in range(length, n, length))
            if all(seqs):
                invalid2 += x
                # print(num)
                break
        

print(invalid1, invalid2)


