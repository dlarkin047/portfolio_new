# -----------------------------------------------------------------
# Run commands
# -----------------------------------------------------------------
# Bulk renames: python rename_files.py <bulk option> <input dir> <new file name>
# Bulk Options: b, bulk, B, BULK
# E.g.  python rename_files.py b ./test_files/ new_file_name
# -----------------------------------------------------------------
# Individual renames : python rename_files <source file> <file rename>
# E.g.  python rename_files.py ./test_files/rew_1.txt new_file_name
# -----------------------------------------------------------------

import os
import sys
import pathlib

divider = '---------------------------------------------------------------'

def rename(bulk, src, dest):
    print(str(bulk) +' : '+ src +' : '+dest)
    if bulk:
        i=0
        for file in os.listdir(src):
            p_file = ''.join([src,file])
            new_f_name = '.'.join([dest+'_'+str(i), file.split('.')[1]])
            new_f = ''.join([src,new_f_name])
            os.rename(p_file, new_f)
            print(divider)
            print(file +" renamed to: " + new_f_name)
            i+=1
    else:
        src = pathlib.Path(src)
        dest = '.'.join([dest.split('.')[0], src.name.split('.')[1]])
        new_f = os.path.join(src.parent, dest)

        print(divider)
        print(f'{src.name} renamed to: {dest}\nPlease check directory {new_f}')
        os.rename(src, new_f)

def main():
    if len(sys.argv) > 3:
        if (sys.argv[1] == 'b' or sys.argv[1] == 'bulk' 
            or sys.argv[1] == 'B' or sys.argv[1] == 'BULK') :
            rename(True, sys.argv[2], sys.argv[3])
        else:
            print("Invalid Options provided. Please input the correct arguments.")
            exit()
        print()
    elif len(sys.argv) > 2:
        rename(False, sys.argv[1], sys.argv[2])
        print()
    else:
        bulk = int(input("Please choose from the following options:\n\t1)\tBulk rename\n\t2)\tIndividual rename\n"))
        if bulk == 1 :
            bulk = True
        elif bulk == 2 :
            bulk = False
        else :
            print("Please choose valid options. Try again")
            exit()
        src = input("File you wish to rename (path and filename and extension e.g. ./example_folder/example_file.txt ):\n")
        dest = input("Please provide a name you wish to rename the file to:\n")
        rename(bulk, src, dest)
    print(divider)

if __name__ == '__main__':
    main()