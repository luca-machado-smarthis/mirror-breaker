level_map1 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ', #Sempre botar esse layer superior para evitar sair pulando para fora da tela
    'x                                  xxxxxxxx   ',
    'x                          M       xxxxxxxx   ',
    'xM     xxx    xxx       xxxx       xxxxxxxx   ',
    'xxx                  s             xxxxxxxx   ',
    'x                  xxx             xxxxxxxx   ',
    'x s       xxx                        xxxxxx   ',
    'x xx             M                  Exxxxxx   ',
    'x       xx      xx           xxxxxxxxxxxxxx   ',
    'x               xx   ss      xxxxxxxxxxxxxx   ',
    'x  P                 xx      xxxxxxxxxxxxxx   ',
    'xxxxxxxxxxxx xx              xxxxxxxxxxxxxx   ',
    'x          x xx              x            x   ' #Sempre botar esse layer inferior para caso esteja deslizando pela parede so morre quando o boneco todo cair da tela
]

tile_size = 56
screen_width = 1200
screen_height = 11 * tile_size #numeros de linhas totais em todos as fases

level_maps = [level_map1, level_map1,0,0,0,0,0,0,0,0] #Botei o mapa um no level2 so para testar o level_select
