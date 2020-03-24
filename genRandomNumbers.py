#!/usr/bin/env python
import argparse
import string
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=int, default=5, help="Number of dirs at each depth")
parser.add_argument("-f", "--files", type=int, default=5, help="Max number of files to make")
parser.add_argument("-l", "--location", type=str, default='.', help="Location to make the folders")
parser.add_argument("-s", "--size", type=int, default=5, help="Length of file name sizes")
parser.add_argument("-c", '--contents', type=int, default=50, help="Max number of letters in the file")
parser.add_argument("--depth", type=int, default=2, help="depth of the file tree")
args = parser.parse_args()
root = args.location + "/randomFiles/"


def gen_files(location, currentDepth):
    # Generate some files
    makeFiles(location, location)
    # If we are at the desired depth return
    if currentDepth == args.depth:
        return
    # Generate the dirs
    for d in range(0, args.dir):
        dirName = None
        # Make the file and make sure it does not match a file we already made
        while dirName is None or (not os.path.exists(location + dirName)):
            dirName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=args.size))
            os.mkdir(location + dirName)
            print("tying to make file: " + location + dirName)
        # Make the files in this dir recursively
        gen_files(location + dirName + "/", currentDepth + 1)


def makeFiles(location, dirName):
    for f in range(0, args.files):
        fileName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=args.size))
        fileContents = ''.join(random.choices(string.ascii_uppercase + string.digits, k=args.contents))
        print("Writing: " + fileContents + " to: " + location + fileName + ".txt")
        f = open(location + fileName + ".txt", "w")
        f.write(fileContents)
        f.close()


if __name__ == "__main__":
    # Make the root folder to put all the generated folders
    if not os.path.exists(root):
        os.mkdir(root)
    # Start the recursion
    gen_files(root, 0)
