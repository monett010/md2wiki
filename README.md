# Md2Wiki
Converts Markdown files to WikiMedia format

## Setup
```bash
chmod +x md2wiki.py

sudo cp md2wiki.py /usr/bin/md2wiki
```

## Use
To convert one Markdown file to wiki:
```bash
md2wiki filename.md
```

To convert a whole directory of Markdown files, navigate to the directory containing the files, and type:
```bash
md2wiki
```
The .wiki files will be in a directory called ``wikifiles``.



## Requirements
* Python 3

* Linux

* [Pandoc](https://pandoc.org/installing.html)