# Ace_todolist

This is TODO APPLICATION & Python CLI application


## Installation

you can install Ace_todolist using pip

```
pip install Ace_todolist
```

## Precautions

#### first

```
pip list
```

If you confirm the list of pip, the application may be named `Ace-todolist`.

Sorry, but if you run the application, please `Ace_todolist` not `Ace-todolist`.


#### second

We miss coding the path of db. (The db name is ace.db)

Sorry, it will be fixed soon.


## User Guide

```
$ Ace_todolist

Hello!, This is ACE TODO APPLICATION
If you want to run action of ACE, confirm options(-h or --help)

```

If you want to run action of Ace_todolist, confirm options(-h or --help)

```
$ Ace_todolist --help

usage: Ace_todolist [-h] [--add] [--list] [--edit] [--stat] [--search]
                    [--detail] [--remove] [--version]

optional arguments:
  -h, --help  show this help message and exit
  --add       add item
  --list      print list of items
     a         print all list
     f         print finished and unfinished list separately
  --sort      sort the list of items (must be used with --list)
     t, T      sort by Title
     c, C      sort by Category
     p, P      sort by Priority
     d, D      sort by Due
               * Lowercase letter sort by ascending, and uppercase do by descending
  --edit      edit item implemented by option
     title
     category
     due
     priority
     fin
     place
     comment
  --stat      stats of database
  --search    search item that you want to find
     i         by ID
     t         by Title
     c         by Category
     d         by Due
  --detail    print details of items that you want to see
  --remove    remove item that you want to remove
  --version   show program's version number and exit
```
