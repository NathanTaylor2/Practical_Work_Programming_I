import os
import shutil

print("Current directory is", os.getcwd())

os.chdir('FilesToSort')
print(os.listdir('.'))

try:
    os.mkdir('doc')
    os.mkdir('docx')
    os.mkdir('gif')
    os.mkdir('jpg')
    os.mkdir('png')
    os.mkdir('txt')
    os.mkdir('xls')
    os.mkdir('xlsx')
except WindowsError:
    pass


for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        if filename[-4:] == '.doc':
            print(filename, 'moved to doc')
            shutil.move(filename, 'doc/')
        elif filename[-5:] == '.docx':
            print(filename, 'moved to docx')
            shutil.move(filename, 'docx/')
        elif filename[-4:] == '.gif':
            print(filename, 'moved to gif')
            shutil.move(filename, 'gif/')
        elif filename[-4:] == '.jpg':
            print(filename, 'moved to jpg')
            shutil.move(filename, 'jpg/')
        elif filename[-4:] == '.png':
            print(filename, 'moved to png')
            shutil.move(filename, 'png/')
        elif filename[-4:] == '.txt':
            print(filename, 'moved to txt')
            shutil.move(filename, 'txt/')
        elif filename[-4:] == '.xls':
            print(filename, 'moved to xls')
            shutil.move(filename, 'xls/')
        elif filename[-5:] == '.xlsx':
            print(filename, 'moved to xlsx')
            shutil.move(filename, 'xlsx/')
            

