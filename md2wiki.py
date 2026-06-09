#!/usr/bin/env python3

import os
import subprocess


# Converts md file to .wiki
def convert_file (filename)->None:
    dest_file = f"{os.path.splitext(filename)[0]}.wiki"
    cmd = ["pandoc", "-f", "markdown", "-t", "mediawiki", filename, "-o", dest_file]
    subprocess.run(cmd)

# Counts total number of md files in directory
def count_md_files () -> int:
    dir_files = os.listdir()
    md_files = []

    for file in dir_files:
        if (os.path.isdir(file) != True and os.path.splitext(file)[1] == ".md"):
            md_files.append(file)
    return len(md_files)

# Converts all md files in directory to wiki
def convert_directory ()->None:
    dir_files = os.listdir()

    counter = 1
    total_files = count_md_files()

    for file in dir_files:
        if (os.path.isdir(file) != True and os.path.splitext(file)[1] == ".md"):
            convert_file(file)
            print (f"Converting file [{counter}/{total_files}]")
            counter = counter + 1


# Converts the directory and moves the files to directory called "wikifiles"
convert_directory()

if (os.path.isdir("wikifiles") != True):
    subprocess.run(["mkdir", "wikifiles"])
print ("Moving files...")
subprocess.run("mv *.wiki wikifiles",shell=True)