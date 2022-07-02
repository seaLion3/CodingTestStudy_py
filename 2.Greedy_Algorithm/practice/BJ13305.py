n = int(input())
lstlength = list(map(int, input().split()))
lstCost = list(map(int, input().split()))

""" res = lstlength[0] * lstCost[0]
m = lstCost[0]
dist = 0

for i in range(1, n-1):
    if lstCost[i] < m:
        res += m*dist
        dist = lstlength[i]
        m = lstCost[i]
    else:
        dist += lstlength[i]
    
    if i == n-2:
        res += m*dist

print(res) """

res = 0
m = lstCost[0]
for i in range(n-1):
    if lstCost[i] < m:
        m = lstCost[i]
    res += m * lstlength[i]

print(res)