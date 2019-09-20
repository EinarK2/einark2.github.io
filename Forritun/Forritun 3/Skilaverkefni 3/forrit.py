# Einar Karl Pétursson
# 20/9/2019
from nemar import Nemi
from nemar import Grunnskolanemi
from nemar import Framhaldsskolanemi
from nemar import Haskolanemi

nemi1 = Nemi('2609022450', 'Einar Karl Pétursson', 'kk',
             'Álfaheiði 18', '6948820', 'einarkarlp@gmail.com')
print("NEMI")
print(nemi1)
print("-"*35)

grunnskolanemi1 = Grunnskolanemi('2609022450', 'Einar Karl Pétursson', 'kk',
                                 'Álfaheiði 18', '6948820', 'einarkarlp@gmail.com',
                                 'Pétur Óli Einarsson', 'Álfhólsskóli')
print("GRUNNSKÓLANEMI")
print(grunnskolanemi1)
print("-"*35)

framhaldsskolanemi1 = Framhaldsskolanemi('2609022450', 'Einar Karl Pétursson',
                                         'kk', 'Álfaheiði 18', '6948820',
                                         'einarkarlp@gmail.com', 'Tölvubraut', 'Nei')
print("FRAMHALDSSKÓLANEMI")
print(framhaldsskolanemi1)
print('-'*35)

haskolanemi1 = Haskolanemi('2609022450', 'Einar Karl Pétursson', 'kk', 'Álfaheiði 18',
                           '6948820', 'einarkarlp@gmail.com', 'PHd', 'Já')
print("HÁSKÓLANEMI")
print(haskolanemi1)
