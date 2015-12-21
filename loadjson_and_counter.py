#!/usr/bin/python
#coding:utf-8
import json
from collections import Counter
path = 'loadjson_and_counter.json'
with open(path) as f:
    records = [json.loads(line) for line in f]
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    counts = Counter(time_zones)
    print counts.most_common(10)

