LEVELS = [
    [
        '##################################',
        '#                #        #      #',
        '#   G       #|####    K   #      #',
        '#           # et #        #      #',
        '#           # c  #      k #    S #',
        '# ########  ######   H.   #      #',
        '#                #   .    |      #',
        '#         k      /   .    #  S   #',
        '#                #        #      #',
        '##################################'
    ],
    []
]

for level_num in range(len(LEVELS)):
    LEVELS[level_num] = [list(line) for line in LEVELS[level_num]]
