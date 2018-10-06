# TL;DR

This repo contains python codes used in [my answer](https://teratail.com/questions/149275#reply-224709) for the [question No.149275](https://teratail.com/questions/149275) of [teratail](https://teratail.com/), which is a Programming Q&A site of Japan.

# How to run

- git clone git@github.com:jun68ykt/q149275.git
- cd q149275
- chmod +x data_gen.py
- chmod +x make_map.py
- chmod +x count.py
- export PATH=${PATH}:.
- generating data file: data_gen.py > data.txt
- generating map file: cat data.txt | make_map.py > data.map.json
- count names: cat data.map.json | count.py
