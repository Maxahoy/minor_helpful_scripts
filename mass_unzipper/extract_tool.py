import os
import zipfile
import argparse
from pyunpack import Archive
#import patool #not required strictly, but will install when you install pyunpack

"""
Have you ever tried downloading mass files from google drive? I have!

The behavior that gdrive uses when serving files over a certain size is to
split them into ~2gig chunks, and serve them piecemeal. Which works great
until you need to spend some tediuous time unzipping them.

This script just unzips a bunch of files in the directed folder, and can also accept whatever
file extension and directory, and deletion / cleanup behavior you desire as a command line arg.

As you can see by the folder I originally used it on, I was re-downloading my skyrim mods folder.
I'll let you guess how large that was haha

Note that by default, the behavior of the 'extractall' function
is to overwrite & replace any files that already exist somewhere.

So doing this operation multiple times won't hurt anything.



Behavior:

Default behavior running using "python3 extract_tool.py" runs the tool
in the same directory, looking for zip files, and doesn't delete the files afterwards.
Look

python3 extract_tool.py [-t target_dir] [-e extension] [-r]

for example:

python3 extract_tool.py -t E:\\Skyrim Mods\\MO2 Folders -e .zip -r

will run this in my skyrimg mods folder, work on zip files, and remove the old downloads when done.

Supported archive types in the default extension list
-

- Maxwell

"""

default_extension_list = [".zip", ".7z"]

def main(args):
    folder = os.getcwd()
    extension_list = default_extension_list
    delete = False

    
    if args.target:
        folder = args.target
        os.chdir(folder)

    if args.extension:
        extension_list = []
        extension_list.append(args.extension)

    if args.remove:
        delete = args.remove


    for item in os.listdir(folder):
        for ext in extension_list:
            if item.endswith(ext):
                file_name = os.path.abspath(item)
                zip_ref = Archive(file_name)
                zip_ref.extractall(folder)
                #zip_ref.close()
                #closure is unnecessary using pyunpack
                if delete:
                    os.remove(file_name)
                    print(file_name, "was extracted and removed.")
                else:
                    print(file_name, "was extracted.")

def fn_zip(filename):
    pass

def fn_7z(filename):
    pass


if __name__ == "__main__":
   
   argParser = argparse.ArgumentParser()
   argParser.add_argument("-t", "--target", help="Target directory for mass unzip")
   argParser.add_argument("-e", "--extension", help="File extension to look for.")
   argParser.add_argument("-r", "--remove", action="store_true", help="Optional flag to remove all old files.")
   args = argParser.parse_args()
   main(args)

        

