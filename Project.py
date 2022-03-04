import os ,shutil

from_path = '/Users/shreyjkatrodiya/Downloads'

to_path = '/Users/shreyjkatrodiya/Desktop/Python/Pro-102/pdf_files'

list_files = os.listdir(from_path)

for file in list_files:
    name,ext = os.path.splitext(file)
    if ext == '.pdf':
        source_path=from_path+'/'+file
        shutil.move(source_path,to_path)
    
