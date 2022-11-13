level_map1 = [
    'x                       xxxxxxxxxxxx   ',
    'x   xxx                 xxxxxxxxxxxx   ',
    'x      xxx    xxx       xxxxxxxxxxxx   ',
    'xxx                    xxxxxxxxxxxx   ',
    'x                       xxxxxxxxxxxx   ',
    'x                       xxxxxxxxxxxx   ',
    'x                       xxxxxxxxxxxx   ',
    'x              xx            xxxxxxxxxxxx   ',
    'x  xx          xx            xxxxxxxxxxxx   ',
    'x  P             xx            xxxxxxxxxxxx   ',
    'xxxxxxxxxxxx xxx             xxxxxxxxxxxx   ',
]

tile_size = 56
screen_width = 1200
screen_height = len(level_map1) * tile_size

level_maps = [level_map1, level_map1,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select