#!/usr/bin/env python3

import json
import sys
from mod import count

m = json.load(sys.stdin)

result = {}

for t in m["data"]:
    name = m["symbols"][t[0]]
    if name in result:
        continue
    result[name] = count(t[0], m["indexes"], m["data"])

for k, v in sorted(result.items()):
    print("%s: %d" % (k, v))
