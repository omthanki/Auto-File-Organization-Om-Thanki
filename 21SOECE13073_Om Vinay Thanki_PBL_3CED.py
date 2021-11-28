import os
import time
import os.path
import shutil
import gui

def file_extension(f):
    split_tup = os.path.splitext(f)
    return split_tup[1]

def directory_exists(temp_dest):
    return os.path.isdir(temp_dest)

def create_directory(d, dir):
    path=os.path.join(d, dir)
    os.mkdir(path)

def file_exists(f):
    return os.path.exists(f)

def movefile(s, d):
    shutil.move(s, d)


def extension_wise(source, destination):
    source += '/'
    destination += '/'

    for f in os.listdir(source):

        extension=(file_extension(f))
        extension=extension[1:]

        if extension == '':
            continue

        if not(directory_exists(destination + extension)):
            create_directory(destination, extension)

        s = source + f
        d = destination + extension + '/' + f

        if file_exists(d):
            print(f, " already exists")
            continue

        movefile(s, d)


def category_wise(source, destination):
    source += '/'
    destination += '/'

    for f in os.listdir(source):

        extension=(file_extension(f))
        extension=extension[1:]
        extension=extension.lower()

        if extension == 'pdf' or extension == 'docx' or extension == 'xlsx' or extension == 'pptx':
            folder = 'Documents'
        elif extension == 'jpeg' or extension == 'jpg' or extension == 'png':
            folder = 'Images'
        elif extension == 'mp3' or extension == 'mp4':
            folder = 'Vidoes'
        elif extension == 'txt':
            folder = 'Text Files'
        elif extension == 'rar' or extension == 'zip':
            folder = 'Zip Files'
        elif extension == 'exe':
            folder = 'Executable Files'
        elif extension == 'c' or extension == 'py' or extension == 'ipynb' or extension == 'cpp' or extension == 'php' or extension == 'html' or extension == 'css' or extension == 'java':
            folder = 'Programs'
        else:
            folder = 'Uncategorized'

        temp = destination + folder

        if not(directory_exists(temp)):
            create_directory(destination, folder)

        s = source + f
        d = destination + folder + '/' + f

        if file_exists(d):
            print(f, " already exists")
            continue

        movefile(s, d)


def time_wise(source, destination):
    source += '/'
    destination += '/'

    for f in os.listdir(source):

        time1 = os.path.getmtime(source + f)

        time2=time.ctime(time1)

        year = time2[-4:]
        month = time2[4:7]
        date = time2[8:10]

        if not(directory_exists(destination + year)):
            create_directory(destination, year)

        if not(directory_exists(destination + year + '/' + month)):
            create_directory(destination + year, month)

        if not(directory_exists(destination + year + '/' + month + '/' + date)):
            create_directory(destination + year + '/' + month, date)

        s = source + f
        d = destination + year + '/' + month + '/' + date + '/' + f

        if file_exists(d):
            print(f, " already exists")
            continue

        movefile(s, d)


source = gui.source
destination = gui.destination
choice = gui.choice

if choice == 'Extension Wise':
    extension_wise(source, destination)
elif choice == 'Category Wise':
    category_wise(source, destination)
elif choice == 'Time Wise':
    time_wise(source, destination)
else:
    print("Invalid Choice")