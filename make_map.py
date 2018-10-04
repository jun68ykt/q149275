#!/usr/bin/env python3

import sys

data = []
symbols = []

for line in sys.stdin:
    if line[0] == '#':
        continue

    tokens = line.split()
    if not len(tokens) == 2:
        continue

    t = [-1, -1]

    for i, _ in enumerate(t):
        if tokens[i] in symbols:
            t[i] = symbols.index(tokens[i])
        else:
            symbols.append(tokens[i])
            t[i] = len(symbols) - 1

    data.append(t)


indexes = [[] for _ in range(len(symbols))]

for i, t in enumerate(data):
    indexes[t[0]].append(i)
    indexes[t[1]].append(i)


# JSON出力
print("{")
print("  \"symbols\": [%s]," % (', '.join([("\"%s\"" % s) for s in symbols])))
print("  \"data\": [")
for i, t in enumerate(data):
    print("    [%d, %d]%s" % (t[0], t[1], ',' if i < len(data)-1 else ''))
print("  ],")
print("  \"indexes\": [")
for i, ary in enumerate(indexes):
    print("    %s%s" % (str(ary), ',' if i < len(indexes)-1 else ''))
print("  ]")
print("}")
