#!/usr/bin/env python3

import random
import sys

DEFAULT_NUM_NAMES = 5
MAXIMUM_NUM_NAMES = 26
DEFAULT_NUM_CODES = 10
MAXIMUM_NUM_CODES = 30

# names
if len(sys.argv) > 1:
    try:
        num_names = int(sys.argv[1])
        if num_names <= 0 or num_names > MAXIMUM_NUM_NAMES:
            num_names = DEFAULT_NUM_NAMES
    except ValueError:
        num_names = DEFAULT_NUM_NAMES
else:
    num_names = DEFAULT_NUM_NAMES

names = [chr(x) for x in range(ord('A'), ord('A') + num_names)]

print("# names: %s" % names)

# num_codes
if len(sys.argv) > 2:
    try:
        num_codes = int(sys.argv[2])
        if num_codes <= 0 or num_codes > MAXIMUM_NUM_CODES:
            num_codes = DEFAULT_NUM_CODES
    except ValueError:
        num_codes = DEFAULT_NUM_CODES
else:
    num_codes = DEFAULT_NUM_CODES

print("# num_codes: %d" % num_codes)

# num_data
num_data = int(len(names) * num_codes / 2.5)

print("# num_data: %d\n" % num_data)


# generating data

data = []

while True:
    if len(data) == num_data:
        break
    name = random.choice(names)
    code = 'X-%02d' % (1 + random.randrange(num_codes))
    if not (name, code) in data:
        data.append((name, code))

for t in data:
    print('%s\t%s' % t)
