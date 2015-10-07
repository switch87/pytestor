import os
import re
from termcolor import colored
from refactor.test_files import TestFile

test_files = []
rootdir = '/home/switch87/workspace/mvne-platform'

for dir_name, subdir_list, file_list in os.walk(rootdir):
    for file in file_list:
        if re.match(r'^.*test.*.py$', file) is not None and not '__pycache__' in dir_name:
            newfile = TestFile(file, dir_name)
            test_files.append(newfile)

for file in test_files:
    print(file.get_full_name())
    print('-'*len(file.get_full_name()))
    for line in file.lines:
        if line.assertion is not None:
            print(colored(str(line.line_nr)+' - '+line.assertion.line[:-1], 'green'))
        else:
            if 'self.assert' in line.line:
                print(colored(str(line.line_nr)+' - '+str(line.line[:-1]),'red'))
            else:
                print(str(line.line_nr)+' - '+str(line.line[:-1]))
    print()

    file.replace_file()
