import os
from datetime import datetime
print(dir(os))

#cria diretorio
try:
    os.mkdir('./dir-prog10/')
except:
    pass
#criando multiple directories
try:
    os.makedirs('./dir-prog10/sub-dir/sub-2-dir')
except:
    pass

# remove diretorio
#os.removedirs('./dir-prog10/')

#data de criacao
data = datetime.fromtimestamp(os.stat('prog03.py').st_mtime)
print(data)

#size
print(os.stat('prog02.py').st_size)

#listar os arquivos e diretorios
print(os.listdir())

# Para ver toda a árvore de diretórios e arquivos dentro
# os.walk é um gerador que produz uma tupla de 3 valores conforme percorre a árvore de diretórios
for dirpath, dirname,files in os.walk('./'):
    print(dirpath,dirname,files)

"""
os.path.dirname(‘/tmp/test.txt’)
# retorna o diretorio /tmp

os.path.split(‘/tmp/test.txt’)
# retorna o diretório e o arquivo como um Énuplo

os.path.exists(‘/tmp/test.txt’)
# retorna um booleano

os.path.isdir(‘/tmp/test.txt’)
# retorna false 

os.path.isfile(‘/tmp/test.txt’)
# returna true

"""

