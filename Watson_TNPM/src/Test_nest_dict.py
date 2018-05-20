
from collections import defaultdict

target_dict = defaultdict(dict)
target_dict['key1']['key2'] = 'val12'

for k,v in target_dict.items():
    for k1,v2 in v.items():
        print(k)
        print(k1)