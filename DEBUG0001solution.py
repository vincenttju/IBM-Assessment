n = input()
allValid = True
errorcodes = []
for i in range(int(n)):
    inp = input().split(" ")
    if (inp[1] == "false"):
        allValid = False
        errorcodes.append(inp[2])

if(allValid):
    print("Yes")
    print([])
else:
    print("No")
    joined_string = ' '.join([str(v) for v in errorcodes])
    print(joined_string)