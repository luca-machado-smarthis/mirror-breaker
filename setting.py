level_map1 = [
    'x                                  xxxxxx   ',
    'x                        M         xxxxxx   ',
    'xM     xxx    xxx     xxxx         xxxxxx   ',
    'xxx                 s              xxxxxx   ',
    'x                 xxx              xxxxxx   ',
    'x s      xxx                       xxxxxx   ',
    'x xx            M                 Exxxxxx   ',
    'x              xx            xxxxxxxxxxxx   ',
    'x      xx      xx   ss       xxxxxxxxxxxx   ',
    'x  P                xx       xxxxxxxxxxxx   ',
    'xxxxxxxxxxxxxxx              xxxxxxxxxxxx   ',
]

tile_size = 56
screen_width = 1200
screen_height = len(level_map1) * tile_size

level_maps = [level_map1, level_map1,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select
