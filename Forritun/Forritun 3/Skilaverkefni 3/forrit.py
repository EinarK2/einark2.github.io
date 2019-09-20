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

grunnskolanemi1 = Grunnskolanemi('1234567890', 'Jón Jónsson', 'kk',
                                 'Hlíðarhjalli 39', '1234567', 'jon@jon.is',
                                 'Jón Jóhannesson', 'Álfhólsskóli')
print("GRUNNSKÓLANEMI")
print(grunnskolanemi1)
print("-"*35)

framhaldsskolanemi1 = Framhaldsskolanemi('0987654321', 'Jónína Jónsdóttir',
                                         'kvk', 'Skipholt 6', '7654321',
                                         'jonina@mail.com', 'Tölvubraut', 'Nei')
print("FRAMHALDSSKÓLANEMI")
print(framhaldsskolanemi1)
print('-'*35)

haskolanemi1 = Haskolanemi('2609022450', 'Pétur Karl Einarsson', 'kk', 'Álfaheiði 19',
                           '6969920', 'peturkarle@gmail.com', 'PHd', 'Já')
print("HÁSKÓLANEMI")
print(haskolanemi1)
