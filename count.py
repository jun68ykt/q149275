#!/usr/bin/env python3

import json
import sys


def count(name_id, indexes, data):
    name_index_ary = indexes[name_id]
    cnt = len(name_index_ary)

    for i in name_index_ary:
        code_id = data[i][1]
        code_index_ary = indexes[code_id]
        a = [j for j in code_index_ary if j > i]
        cnt += len(a)

    return cnt


m = json.load(sys.stdin)

result = {}

for t in m["data"]:
    name = m["symbols"][t[0]]
    if name in result:
        continue
    result[name] = count(t[0], m["indexes"], m["data"])

for k, v in sorted(result.items(), key=lambda x: -x[1]):
    print("%s: %d" % (k, v))
