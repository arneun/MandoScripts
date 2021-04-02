from os import listdir
import shutil
from os.path import isfile, join, exists, basename
import sys
import os
from pathlib import Path

# przydatne funkcje:

# wszystkie foldery/pliki w danym katalogu
def all_inside(path, is_file):
    inside = []
    for entry in listdir(path):
        if(is_file == isfile(path + '/' + entry)):
            inside.append(entry)
    return inside

# wszystkie foldery w katalogu
def author_folders(path):
    return all_inside(path, False)

# lista: (autor (folder), lista plików) 
def author_pictures(path, folders):
    author_pictures_list = []
    for folder in folders:
        author_pictures_list.append((folder, [path+ '/' + folder + '/' + res for res in all_inside(path + '/' + folder, True)]))   
      
    return author_pictures_list

# li
def create_copy_list(destination, name_prefix, files_list, extension):
    copy_list = []
    for i, file in enumerate(files_list):
       # print(file)
        copy_list.append((file, name_prefix + str(i) +extension, destination + '/' + name_prefix + str(i) +extension))
    return copy_list

def create_page_text(pictures):
    page_entries = []
    text_format = '''<a href='/mywakcji/{picture}' rel='lightbox[to_replace_1]' title='to_replace_2'><img src='/mywakcji/{picture}'></a>'''
    for picture in pictures:
        page_entries.append(text_format.format(picture=picture))
    return page_entries

arg = sys.argv

target_folder = arg[1]

# folder startowy musi istnieć
if(target_folder is not None and exists(target_folder)):
    
    # foldery autorów
    files = author_folders(target_folder)
    #combos autor - lista plików
    authors_pics = author_pictures(target_folder, files)
    
    # lista do kopiowania
    copy_list = []
    
    # łapiemy nazwę konwentu (nazwę folderu startowego)
    con_name = basename(target_folder)
    
    destination_folder = target_folder + '/' + con_name

    # tworzymy listę kopiowania
    for (author, pics) in authors_pics:
         copy_list += create_copy_list(destination_folder, con_name + '_' + author + '_', pics, '.jpg')

    # tworzenie folderu docelowego jeśli nie istnieje (wypieprzy się jeśli nie będzie folderu docelowego)
    if(not exists(destination_folder)):
        os.mkdir(destination_folder)
    
    # właściwe kopiowanie na podstawie listy 
    for (src, pic, dest) in copy_list:
        print(src,  dest)
        shutil.copyfile(src,  dest)
    
    # tworzymy wpisy do pliku z którego można skopiować na stronę
    pic_list = [pic for (src, pic, des) in copy_list]
    with open(destination_folder + '/kod_na_strone.txt', 'w') as f:
       for entry in create_page_text(pic_list):
           f.write(entry + '\n')
           print(entry)
else:
    print("To nie ścieżka do folderu, nic się nie da zrobić (albo brakuje uprawnień)")

