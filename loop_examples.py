list1 = ["element1", "element2", "element3"]
list2 = ["element4", "element5", "element6", "element7"]

for i, j in zip(list1, list2):
    print i,j

for i in reversed(list1):
    print i

for i, j in enumerate(list1):
    print i, j,


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

list_comprehension_data = [data for data in raw_data if not math.isnan(data)]
print filtered_data
print list_comprehension_data