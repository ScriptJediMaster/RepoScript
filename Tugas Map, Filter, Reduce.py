data = list(range(5,21))
map_data = list(map(lambda x: x * 2, data))

filter_data = list(filter(lambda x: x % 4 == 0, map_data))


from functools import reduce
total = reduce(lambda x, y: x + y, filter_data)


print("Mapping setiap angka dikalikan dua:")
print("map_data:", map_data)

print("\nFiltering angka hasil mapping (dengan syarat angka habis dibagi 4):")
print("filter_data:", filter_data)

print("\nReduce dengan cara penambahan secara sequential hasil dari filterisasi:")
print("total:", total)