# %%
import os
from webbrowser import get
import fontTools.ttLib as tt
from typing import List
import string
import shutil

# %%
os.chdir(r'***\Temp')

def get_dirlists():
    dire_lists = os.listdir()
    dirlists = []
    for direc in dire_lists:
        if os.path.isdir(direc):
            dirlists.append(direc)
    return dirlists

dirl = get_dirlists()
len16_dirl = []
for direc in dirl:
    if len(direc) == 16:
        len16_dirl.append(direc)

def get_needed_dir(direc: List) -> List:
    needed_dir = []
    for dire in direc:
        if len(os.listdir(dire)) == 1:
            needed_dir.append(dire+ '\\' + os.listdir(dire)[0])
    return needed_dir

needed_dir = get_needed_dir(len16_dirl)
truly_needed_file = get_needed_dir(needed_dir)

# %%
if os.path.exists('out')==False:
    os.mkdir('out')
for i,files in enumerate(truly_needed_file):
    shutil.copy(files, f'out\\file{i}.otf')

# %%
os.chdir('out')


# %%

from tokenize import Name

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

unnamed_fonts_list = os.listdir()

for ttf in unnamed_fonts_list:
    font = tt.TTFont(ttf)
    names = font['name'].names
    for i in names:
        if i.langID == 33 and len(str(i))>=1 and is_Chinese(str(i)[0:1]):
            name = i
            break
        if i.langID == 1033 and len(str(i))>=1 and is_Chinese(str(i)[0:1]):
            name = i
            break
        if i.langID == 2052 and len(str(i))>=1 and is_Chinese(str(i)[0:1]):
            name = i
            break
    try:
        os.rename(ttf, f'{name}.otf')
    except NameError:
        for i in names:
            if i.langID == 0 and len(str(i))>=1 and str(i)[0] not in string.digits + string.punctuation:
                name = i
                break
        os.rename(ttf, f'{name}.otf')
        

# %%



