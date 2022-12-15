level_map1 = [ #done 15 SEGUNDOS    
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 
    'x                                                 xxxx',
    'x                                            M    xxxx',
    'x                                            x    xxxx',
    'x                                                 xxxx',
    'x                                M       xxxxx    xxxx',
    'xM              xxx             xxx              xxxxx',
    'xxxx            xxx             xxx             xxxxxx',
    'x               xxx             xxx           xxxxxxxx',
    'x      xxx      xxx             xxx                xxx',
    'xM  P           xxxSSSSSSSSSSSSSxxx M             Exxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
]

level_map2 = [ #DONE
    'x                                                    ',
    'x                                                 xxx',
    'x                                   SS            xxx',
    'xES          SSS      S            xxxx       SS Mxxx',
    'xxxxx     xxxxxxxx   xxxxM                   xxxxxxxx',
    'x                        xxxx              SS     xxx',
    'x                                 ss     xxxx     xxx',
    'x                               xxxx              xxx',
    'x                xxxx                             xxx',
    'x            MSS                                  xxx',
    'x   P    xxxxxxxSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]


level_map3 = [ #possiveis ajustes
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'x                                                xxxxx',
    'x                                                xxxxx',
    'x  Mw   G   Gw   w G    w        w     Gw        xxxxx',
    'x  xxxxxxxxxx     xxxxxx          xxxxxx         xxxxx',
    'x                               wG   w           xxxxx',
    'x              M      w  G  w    xxxx   w G  w   xxxxx',
    'x              xxxx    xxxxx             xxxx    xxxxx',
    'x                                                xxxxx',
    'x                                             xxxx  xx',
    'xEw  P  G    M    G       G   M     G    W    G  wM xx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map4 = [
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x                                                 x',
    'x   P                                             x',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

tile_size = 56
screen_width = 1200
screen_height = 11 * tile_size #numeros de linhas totais em todos as fases

level_maps = [level_map3, level_map2,level_map1,level_map1,level_map1,level_map1,level_map1,level_map1,level_map1,level_map1,level_map1,level_map1] #Botei o mapa um no level2 so para testar o level_select
firebreathers_orientations = [[],[],[],[],[],[],[],[],[],[],[],[]]

timer_maps = [2000000,20000,20000,200000,200000,200000,200000,20000,200000,200000,200000,200000]#tempo em milisegundos
