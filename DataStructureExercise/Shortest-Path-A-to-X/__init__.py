from Data import HashTownData
from databuilder import Map_of_town

map = Map_of_town()
places = map.create_map()


for place in places:
    print(f"{place.name} references:")
    for bucket in place.hash_table_town:
        for key,value in bucket:
            print(f" {value.name}")



