import tkinter
import tkinter.filedialog
import os
import shutil
"""First Program(Sorting files in a folder)"""

filePath=tkinter.filedialog.askdirectory()
list_=os.listdir(filePath)
print(list_)
for file in list_:
    ext = os.path.splitext(file)
    print(ext)
    if ext[-1] == '':
        continue
    
    elif os.path.exists(filePath+'/'+ext[-1]):
        shutil.move(f'{filePath}/{file}',f'{filePath}/{ext[-1]}/{file}')

    else:
        os.makedirs(f'{filePath}/{ext[-1]}')
        shutil.move(f'{filePath}/{file}',f'{filePath}/{ext[-1]}/{file}')