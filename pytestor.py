# pytestor is a refactoring tool to replace assertions for use with pytest
# Copyright (C) 2015  Gert Pellin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
import re
import argparse
from termcolor import colored
from refactor.test_files import TestFile


def command_parser():
    parser = argparse.ArgumentParser(description='Refactor a project to use Pytest.')
    parser.add_argument('directory', metavar='DIR', type=str, help='The project directory')

    return parser.parse_args()


def process_directory(directory):
    cwd = re.split(r'/',os.getcwd())

    while re.match(r'^../.*',directory):
        cwd = cwd[:-1]
        directory = directory[3:]

    if re.match(r'^./.*', directory):
        directory = directory[2:]
    elif re.match(r'~/.*', directory):
        directory = os.getenv("HOME") + '/' + directory
    if not re.match(r'/.*', directory):
        directory = '/'.join(d for d in cwd) + '/' + directory
    return directory


def iterate_files(root_directory):
    test_files = []

    for dir_name, subdir_list, file_list in os.walk(root_directory):
        for file in file_list:
            if re.match(r'^.*test.*.py$', file) is not None and not '__pycache__' in dir_name:
                newfile = TestFile(file, dir_name)
                test_files.append(newfile)
    return test_files

args = command_parser()
root_dir = process_directory(args.directory)
test_files = iterate_files(root_dir)

imports = []

for file in test_files:
    print(file.get_full_name())
    print('-'*len(file.get_full_name()))
    for line in file.lines:
        if line.assertion is not None:
            print(colored(str(line.line_nr)+' - '+line.get_refactor(), 'green'))
        else:
            if 'self.assert' in line.line:
                print(colored(str(line.line_nr)+' - '+line.get_refactor(),'red'))
    print()
    if file.import_pytest:
        imports.append(file)
    file.replace_file()

for file in imports:
    print(file.get_full_name())