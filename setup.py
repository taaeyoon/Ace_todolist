from setuptools import setup, find_packages
from glob import glob
import os

def find_dirs(dir_name):
    for dir, dirs, files in os.walk('.'):
        if dir_name in dirs:
            yield os.path.relpath(os.path.join(dir, dir_name))

# Find all of the man/info pages
data_files = []
man_sections = {}
for dir in find_dirs('man'):
    for file in os.listdir(dir):
        section = file.split('.')[-1]
        man_sections[section] = man_sections.get(section, []) + [os.path.join(dir, file)]
for section in man_sections:
    data_files.append(('share/man/man'+section, man_sections[section]))
info_pages = {}
for dir in find_dirs('info'):
    for file in glob(os.path.join(dir, '*.info')):
        info_pages[dir] = info_pages.get(dir, []) + [file]
for dir in info_pages:
    data_files.append(('share/info', info_pages[dir]))

setup(
    name             = 'Ace_todolist',
    version          = '2.0',
    description      = 'todolist by Ace',
    license          = 'MIT',
    author           = 'Ace',
    author_email     = 'qmffhrmdyd123@naver.com',
    url              = 'https://github.com/taaeyoon/Ace_todolist',
    download_url     = 'https://github.com/taaeyoon/Ace_todolist/archive/master.zip',
    #data_files       = [('usr/share/man/man1', ['Ace_todolist.1'])],
    packages         = find_packages(exclude = ['coding_convention', 'repository_rules']),
    keywords         = 'todolist by Ace',
    python_requires  = '>=3.6',
    entry_points     = {
                        'console_scripts': [
                        'Ace_todolist = Ace_todolist.__main__:run_program',
                        ],
                        },
    zip_safe = False,
    classifiers      = [
        'Programming Language :: Python :: 3.6'
    ]
)
