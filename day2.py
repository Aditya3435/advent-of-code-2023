with open('input.txt') as f:
    s = f.read()
    

ans = 0
for game in s.strip().split("\n"):
    ID = game.split()[1][:-1]
    r,g,b = -1,-1,-1
    for sett in game.split(':')[1].split(';'):
        for cube in sett.split(','):
            freq = int(cube.strip().split()[0])
            color = cube.strip().split()[1]
            if color == "red":
                r = max(r, freq)
            elif color == "blue":
                b = max(b, freq)
            else:
                g = max(g, freq)
    print(r*b*g)
    ans += int(r*b*g)
print(ans)