level_map1 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ', #Sempre botar esse layer superior para evitar sair pulando para fora da tela
    'x                                      xxxxxxxx   ',
    'x                             M        xxxxxxxx   ',
    'xM     xxxx    xxxx        xxxx        xxxxxxxx   ',
    'xxxx                    s              xxxxxxxx   ',
    'x                    xxxx              xxxxxxxx   ',
    'x           xxxx                         xxxxxx   ',
    'x                   M                   Exxxxxx   ',
    'x       xxx       xxx            xxxxxxxxxxxxxx   ',
    'x                 xx     ss      xxxxxxxxxxxxxx   ',
    'x  P                    xxx      xxxxxxxxxxxxxx   ',
    'xxxxxxxxxxxx xx                  xxxxxxxxxxxxxx   ',
    'x          x xx                  x            x   ' #Sempre botar esse layer inferior para caso esteja deslizando pela parede so morre quando o boneco todo cair da tela
]

level_map2 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                  P                      xxxxx',
    'xxxxx               xxxxxxxx                  xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxxM                                       Mxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

tile_size = 56
screen_width = 1200
screen_height = 11 * tile_size #numeros de linhas totais em todos as fases

level_maps = [level_map1, level_map2,0,0,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select

timer_maps = [30000,200000,0,0,0,0,0,0,0,0,0,0]#tempo em milisegundos
