from functools import reduce

data = range(1, 11)


map_data = list(map(lambda x: x + 3, data))


filter_data = list(filter(lambda x: x % 2 == 0, map_data))


total = reduce(lambda x, y: x + y, filter_data)


print("Mapping setiap nilai akan ditambah 3:")
print("map_data:", map_data)

print("\nFiltering nilai hasilnya habis dibagi 2 ):")
print("filter_data:", filter_data)

print("\nReduce total semuanya:")
print("total:", total)
