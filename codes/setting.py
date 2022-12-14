level_map1 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ', #Sempre botar esse layer superior para evitar sair pulando para fora da tela
    'x                                      xxxxxxxx   ',
    'x                             M        xxxxxxxx   ',
    'xM     xxxx    xFxx        xxxx        xxxxxxxx   ',
    'xxxx                    s              xxxxxxxx   ',
    '                     xxxx              xxxxxxxx   ',
    '           xxxx                          xxxxx    ',
    'F                   M                   E xxxxx   ',
    'F       xxx       xxx            xxxxxxxxxxxxxx   ',
    'F                 xx     ss      xxxxxxxxxxxxxx   ',
    'F   P                    xxx     xxxxxxxxxxxxxx   ',
    'xxxxxxxxxxxx xx                  xxxxxxxxxxxxxx   ',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #Sempre botar esse layer inferior para caso esteja deslizando pela parede so morre quando o boneco todo cair da tela
]

level_map2 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx               xxxxxxxx                  xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxx                                         xxxxx',
    'xxxxxM    P                                  Mxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

tile_size = 56
screen_width = 1200
screen_height = 11 * tile_size #numeros de linhas totais em todos as fases

level_maps = [level_map1, level_map2,0,0,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select

timer_maps = [2000000,200000,0,0,0,0,0,0,0,0,0,0]#tempo em milisegundos
