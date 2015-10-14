# Copyright (C) 2015  Gert Pellin
import argparse
import os
import re
from refactor.test_files import TestFile


def process_directory(directory):
    cwd = re.split(r'/', os.getcwd())

    while re.match(r'^../.*', directory):
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


def command_parser():
    parser = argparse.ArgumentParser(description='Refactor a project to use Pytest.')
    parser.add_argument('directory', metavar='DIR', type=str, help='The project directory')

    return parser.parse_args()
