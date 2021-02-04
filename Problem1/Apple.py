n = int(input())

ls = sorted(int(i) for i in input().rstrip().split())
s = sum(ls)
lsofweight = []

for i in range(len(ls)):
    sumofsubs = ls[i]
    lsofweight.append(abs(s-2*sumofsubs))
    for j in range(i+1, len(ls)-1):
        sumofsubs += ls[j]
        lsofweight.append(abs(s-2*sumofsubs))
print(lsofweight)
print(min(lsofweight))
