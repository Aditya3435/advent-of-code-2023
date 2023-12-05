with open('input.txt') as f:
    inp = f.read()
    vs = inp.strip().split("\n")
ans = 0
m = len(vs)
n = len(vs[0])

goods = [[[] for _ in range(n)] for _ in range(m)]

def isSymbol(i, j, num):
    if not (0 <= i < m and 0 <= j < n):
        return False
    c = vs[i][j]
    if c == '*':
        goods[i][j].append(num)
    return c != '.' and not c.isdigit()


for i, s in enumerate(vs):
    j = 0
    while j < n:
        num = ""
        start = j
        while j < n and s[j].isdigit():
            num += s[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        # look around in the same line
        isSymbol(i, start-1, num)
        isSymbol(i, j, num)

        # look below and up
        for k in range(start - 1, j+1):
            isSymbol(i-1, k, num)
            isSymbol(i+1, k, num)

for i in range(m):
    for j in range(n):
        nums = goods[i][j]
        if vs[i][j] == '*' and len(nums) == 2:
            ans += nums[0] * nums[1]

print(ans)
