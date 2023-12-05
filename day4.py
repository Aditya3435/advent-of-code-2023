with open("input.txt") as f:
    inp = f.read()
    cards = inp.strip().split("\n")

ans = 0
n = len(cards)
dict = {}
for i, card in enumerate(cards):
    i += 1
    winning = card[card.find(": ")+2:card.find(" | ")].strip().split()
    possibleMatches = card[card.find(" | ") + 3:].strip().split()
    common = [i for i in winning if i in possibleMatches]
    common = len(common)
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    for x in range(i+1, i + common + 1):
        if x in dict:
            dict[x] += dict[i]
        else:
            dict[x] = dict[i]
print(sum(dict.values()))