def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    map = [[0 for x in range(width)] for y in range(height)] 

    #add all other snakes
    for enemy_snake in data['board']['snakes']:
        for enemy_pos in enemy_snake['body']:
            map[ enemy_pos['x'] ][ enemy_pos['y'] ] = 'E'

    #add yourself
    for you in data['you']['body']:
        map[ you['x'] ][ you['y'] ] = 'S'

    #add food
    for food in data['board']['food']:
        map[ food['x'] ][ food['y'] ] = 'F'

    #flip map
    for x in map:
        map[x] = map[x][::-1]
    map = map[::-1]

    return map