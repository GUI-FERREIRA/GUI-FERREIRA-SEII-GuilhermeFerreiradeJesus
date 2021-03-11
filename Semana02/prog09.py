#Modulos
#importando funções de outro modulo

#importando modulo criado na lição anteriror
import prog08 as functions
functions.funcao1()

#importando apenas uma função
from prog08 import funcao1
funcao1()

#importando all modules for this
from prog08 import *
print(funcao2('eai'))
