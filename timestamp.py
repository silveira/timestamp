#!/usr/bin/env python

import argparse
import time
import os
import platform

timeStampFormat = '%Y_%m_%d'

# Given a path to a file return the creation date in a best effort
def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else: # Mac
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError: # Linux
            return stat.st_mtime

def main():
    parser = argparse.ArgumentParser(description='Rename a file to start with its timestamp')
    parser.add_argument('filename', nargs='+')
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--suffix', nargs='?', default='')
    args = parser.parse_args()

    for filename in args.filename:
       creation_epoch = creation_date(filename)
       creation_formated = time.strftime(timeStampFormat, time.localtime(creation_epoch))
       creation = creation_formated
       folder = os.path.dirname(filename)

       if args.suffix == '':
           newfilename = creation_formated + '_' + os.path.basename(filename)
       else:
            newfilename = creation_formated + '_' + args.suffix + '_' + os.path.basename(filename)

       newfile = os.path.join(folder, newfilename)

       if args.execute:
         os.rename(filename, newfile)

       print filename, newfile

    if not args.execute:
	print 'This was a dry run. No file was modified. If you want to rename files use the --execute option.'

if __name__ == "__main__":
        main()
