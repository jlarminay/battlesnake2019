import returnMap
import mapCoordinates

def find_path(data, start, goal):
    width = data['board']['width']
    height = data['board']['height']

    map = returnMap.returnMap(data)

    # dist and visited arrays for visited and unvisited vertices
    dist = [10000 for x in range(width*height)]
    vertices = [i for i in range(width*height)]    
    visited = []
    # remove unreachable vertices
    # hazards = returnMap.returnHazards(map)
    # for hazard in hazards:
    #     if goal == hazard:
    #         return False
    #     val = mapToVertex(hazard, width)
    #     vertices.remove(val)

    # set initial distance to 0 (need conversion method)
    start_index = mapCoordinates.mapToVertex(start)
    dist[start_index] = 0

    while len(vertices) > 0:
        pass
    return 420
    

def distance(start, goal):
    dist_x = abs(start['x'] - goal['x'])
    dist_y = abs(start['y'] - goal['y'])
    return dist_x + dist_y