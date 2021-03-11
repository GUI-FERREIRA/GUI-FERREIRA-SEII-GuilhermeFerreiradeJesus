
## Arquivos

f = open("test.txt", "r")
# f = open("test.txt", "w")
# f = open("test.txt", "a")
# f = open("test.txt", "r+")
#print(f.name)
#print(f.mode)
#f.close()

## Lendo arquivos
#with open("test.txt", "r") as f:
#pass

##Arquivos pequenos
f_contents = f.read()
print(f_contents)

##Big Files:
# f_contents = f.readlines()
# print(f_contents)

##Com linhas extras:
# f_contents = f.readline()
# print(f_contents)
# f_contents = f.readline()
# print(f_contents)

##Sem linhas extras:
# f_contents = f.readline()
# print(f_contents, end = '')
# f_contents = f.readline()
# print(f_contents, end = '')

##Iterando através do arquivo:
# for line in f:
# print(line, end = '')

##Voltando
# f_contents = f.read()
# print(f_contents, end = '')

##Print por characters:
# f_contents = f.read(100)
# print(f_contents, end = '')
# f_contents = f.read(100)
# print(f_contents, end = '')
# f_contents = f.read(100)
# print(f_contents, end = '')

##Iterando através de pequenos pedaços:
# size_to_read = 100
# f_contents = f.read(size_to_read)
# while len(f_contents) > 0:
# print(f_contents)
# f_contents = f.read(size_to_read)

##Iterando através de pequenos pedaços:, com 10 characters:
# size_to_read = 10
# f_contents = f.read(size_to_read)
# print(f_contents, end = '')
# f.seek(0)
# f_contents = f.read(size_to_read)
# print(f_contents, end = '')
# print(f.tell())
# while len(f_contents) > 0:
# print(f_contents, end = '*')
# f_contents = f.read(size_to_read)
# print(f.mode)
# print(f.closed)
# print(f.read())


##Escrevendo arquivos
# with open("test.txt", "r") as f:
# f.write("Test")

###Writing Starts:
# with open("test2.txt", "w") as f:
# pass
# f.write("Test")
# f.seek(0)
# f.write("Test")
# f.seek("R")

##Copiando arquivos
# with open("test.txt", "r") as rf:
# with open("test_copy.txt", "w") as wf:
# for line in rf:
# wf.write(line)