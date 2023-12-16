
# Part 1

# with open('input.txt') as f:
#     lines = f.read().strip().split("\n\n")

# seeds = list(map(int,lines.pop(0).split()[1:]))
# maps = []
# i = 0
# while i < len(lines):
#     maps.append([])
#     temp_map = lines[i].split("\n")
#     temp_map.pop(0)
#     j = 0
#     while j < len(temp_map):
#         maps[-1].append(list(map(int, temp_map[j].split())))
#         j+=1
#     i+=1
    
    
# def findLocation(seed):
#     curr = seed
#     for m in maps:
#         for dest, src, range_len in m:
#             if src <= curr < src+range_len:
#                 curr = dest + (curr - src)
#                 break
#     return curr

# ans = 10000000000
# for seed in seeds:
#     location = findLocation(seed)
#     if(ans > location):
#         ans = location
    
# print(ans)
    
    
# Part 2

with open('input.txt') as f:
    lines = f.read().strip().split("\n\n")

seeds = list(map(int,lines.pop(0).split()[1:]))
maps = []
i = 0
while i < len(lines):
    maps.append([])
    temp_map = lines[i].split("\n")
    temp_map.pop(0)
    j = 0
    while j < len(temp_map):
        maps[-1].append(list(map(int, temp_map[j].split())))
        j+=1
    i+=1
    
    
def findLocation(seed):
    curr = seed
    for m in maps:
        for dest, src, range_len in m:
            if src <= curr < src+range_len:
                curr = dest + (curr - src)
                break
    return curr

ans = 10000000000
for seed in seeds:
    location = findLocation(seed)
    if(ans > location):
        ans = location
    
print(ans)
    