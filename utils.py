# -*- coding: utf-8 -*-

import random

def get_color():
    lista_cores = [(255,255,0), #Yellow
                   (255,215,0), #Gold
                   (0,100,0),   #Dark Green
                   (0,255,0),   #Green
                   (0,0,255),   #Blue
                   (70,130,180),#Steel Blue
                   (0,191,255), #Sky Blue
                   (139,69,19), #Brown
                   (255,69,0),  #Orange
                  ]
    return lista_cores[random.randrange(0,len(lista_cores))]

def get_pos():
    lista_pos = [(-60,-60,315),
                 (300,-60,0),
                 (660,-60,45),
                 (660,300,90),
                 (660,660,135),
                 (300,660,180),
                 (-60,660,225),
                 (-60,300,270),
                ]
    return lista_pos[random.randrange(0,len(lista_pos))]
