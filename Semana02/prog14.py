#Python Tutorial: Automate Parsing and Renaming of Multiple Files
import os

os.chdir('./prog14')

# verificar diretorio atual
print(os.getcwd())
# print(dir(os))

# Imprime todos os nomes de arquivo atuais
for f in os.listdir():
    #print(f)
    file_name, file_ext = os.path.splitext(f)
    f_title, f_number = file_name.split('-')
    #print(f_number)
    f_title = f_title.strip()
    f_number = f_number.strip()
    #print('{} = {}'.format(f_title,f_number))
    new_name = '{} = {}'.format(f_title,f_number)
    os.rename(f, new_name)
