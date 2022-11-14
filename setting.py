level_map1 = [
    'x                            xxxxxxxxxxxx   ',
    'x   xxx                  E   xxxxxxxxxxxx   ',
    'x      xxx    xxx     xxxx   xxxxxxxxxxxx   ',
    'xxx                          xxxxxxxxxxxx   ',
    'x                xxx         xxxxxxxxxxxx   ',
    'x        xxx                 xxxxxxxxxxxx   ',
    'x                            xxxxxxxxxxxx   ',
    'x              xx            xxxxxxxxxxxx   ',
    'x  xx          xx            xxxxxxxxxxxx   ',
    'x  P      M         xx       xxxxxxxxxxxx   ',
    'xxxxxxxxxxxxsxxxssssss       xxxxxxxxxxxx   ',
]

tile_size = 56
screen_width = 1200
screen_height = len(level_map1) * tile_size

level_maps = [level_map1, level_map1,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select

mirror_total_maps = [1,0,0,0,0,0,0,0,0,0] #Botar a quantidade de mirrors para cada mapa aqui