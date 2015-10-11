import os
import re
import argparse
from termcolor import colored
from refactor.test_files import TestFile


def command_parser():
    parser = argparse.ArgumentParser(description='Refactor a project to use Pytest.')
    parser.add_argument('directory', metavar='DIR', type=str, help='The project directory')

    return parser.parse_args()


def process_directory(dir):
    cwd = re.split(r'/',os.getcwd())

    while re.match(r'^../.*',dir):
        cwd = cwd[:-1]
        dir = dir[3:]

    if re.match(r'^./.*', dir):
        dir = dir[2:]
    if not re.match(r'/.*', dir):
        dir = '/'.join(d for d in cwd) + '/' + dir
    return dir


def iterate_files(root_dir):
    test_files = []

    for dir_name, subdir_list, file_list in os.walk(root_dir):
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
    if file.import_pytest == True:
        imports.append(file)
    file.replace_file()

for file in imports:
    print(file.get_full_name())