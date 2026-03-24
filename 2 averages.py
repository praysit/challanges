"""
2. Ask for a series of numbers until they want to stop and output the average
"""

nums = []

while True:
    num1 = input()
    if num1 == "stop":
        break
    nums.append(int(num1))

total = 0
for i in nums:
    total += i

print(total / len(nums))