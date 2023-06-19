# from sys import path

# from modulo_import_package.modulo import soma_do_modulo
# from modulo_import_teste import modulo
# from modulo_import_teste.modulo import *

# print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(modulo_import_teste.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)

import modulo_import_package

print(__name__)
modulo_import_package.fala_oi()