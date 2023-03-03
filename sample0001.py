n = input()
strsplit = input().split(" ")
nums = [int(i) for i in strsplit]

sum = 0
for i in nums:
    sum+=i
print(sum) 