from Data import HashTownData
from databuilder import Map_of_town
from collections import deque

def show_map(places):
    for place in places:
        print(place)
        

def count_steps(places,start,end):
    queue = deque()
    queue.append((start, [start.name]))

    visited_place = set()
    visited_place.add(start.name)

    while queue:
        current, path = queue.popleft()
        
        if current.name == end.name:   
            return path
        
        for neighbor in current.connections:
            if neighbor.name not in visited_place:
                visited_place.add(neighbor.name)
                queue.append((neighbor,path + [neighbor.name]))
    return None

map = Map_of_town()
places = map.create_map()

show_map(places)
print()

'''Question: What is the shortest path to school from home?'''


start = places[0]
end = places[3]
quickest_path = count_steps(places, start, end)
print()


if quickest_path:
    print(f"Shortest route from {start.name} to {end.name} is {' '.join(quickest_path)}")
    print(f"Number of steps is {len(quickest_path)}")
else:
    print("Route not found")







