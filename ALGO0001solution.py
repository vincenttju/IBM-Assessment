n = input()
supply = input().split(" ")
m = input()
request = input().split(" ")

if m > n:
    print("No")

# FUNCTION TO SORT INPUTS
def sort_ex(inp, sortarr):
    for i in inp:
        if i[-1] == "S":
            sortarr[0].append(i)
        elif i[-1] == "M":
            sortarr[1].append(i)
        else:
            sortarr[2].append(i)

    sortarr[0].sort(reverse=True)
    sortarr[2].sort()
    extsupply = []
    extsupply.extend(sortarr[0])
    extsupply.extend(sortarr[1])
    extsupply.extend(sortarr[2])
    return extsupply

supplysort = sort_ex(supply,[[],[],[]])
reqsort = sort_ex(request,  [[],[],[]])

convdict = {"L":2, "M":1, "S":0}
curr = len(supplysort)-1
correct = True
for i in range (len(reqsort)-1,-1,-1):
    if convdict[reqsort[i][-1]] <= convdict[supplysort[curr][-1]]:
        curr -= 1
    else:
        print("No")
        correct = False
        break
if(correct):
    print("Yes")

