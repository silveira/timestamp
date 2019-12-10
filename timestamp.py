#!/usr/bin/env python

import argparse
import time
import os
import platform

timeStampFormat = '%Y_%m_%d'
# timeStampFormat = '%Y_%m_%d_%H:%M:%S'

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
    args = parser.parse_args()

    for filename in args.filename:
       creation_epoch = creation_date(filename)
       creation_formated = time.strftime(timeStampFormat, time.localtime(creation_epoch))
       creation = creation_formated
       folder = os.path.dirname(filename)

       #location = 'Iceland'
       # newfilename = creation_formated + '_' + location + '_' + os.path.basename(filename)

       newfilename = creation_formated + '_' + os.path.basename(filename)
       newfile = os.path.join(folder, newfilename)

       os.rename(filename, newfile)

       print filename, newfile

if __name__ == "__main__":
        main()
