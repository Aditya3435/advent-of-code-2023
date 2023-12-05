with open('input.txt') as f:
    s = f.read()

m = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

ans = 0;
for x in s.strip().split("\n"):
    s = ""
    first = None
    last = None
    for c in x:
        y = None
        if c.isdigit():
            y = c
        else:
            s += c
            for string_num, int_num in m.items():
                if s.endswith(string_num):
                    y = str(int_num)
        if y is not None:
            last = y
            if(first is None):
                first = y
    ans += int(first + last)

print(ans)