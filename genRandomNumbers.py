#!/usr/bin/env python
import argparse
import string
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=int, default=5, help="Number of directories to make")
parser.add_argument("-f", "--files", type=int, default=5, help="Max number of files to make")
parser.add_argument("-l", "--location", type=str, default='.', help="Location to make the folders")
parser.add_argument("-s", "--size", type=int, default=5, help="Length of file name sizes")
parser.add_argument("-c", '--contents', type=int, default=50, help="Max number of letters in the file")
args = parser.parse_args()
root = args.location + "/randomFiles/"
if not os.path.exists(root):
    os.mkdir(root)

for d in range(0, args.dir):
    dirName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=args.size))
    while not os.path.exists(root + dirName):
        os.mkdir(root + dirName)
    for f in range(0, random.randrange(0, args.files)):
        print("d: " + str(d) + " f: " + str(f))
        fileName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=args.size))
        fileContents = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=random.randrange(0, args.contents)))
        print(dirName + " " + fileName + " " + fileContents)
