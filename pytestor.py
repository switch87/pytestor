import os
import re
from refactor.test_files import TestFile

test_files = []
rootdir = 'c:\\Users\\gert\\Documents\\workplace\\mvne-platform'

for dir_name, subdir_list, file_list in os.walk(rootdir):
    for file in file_list:
        if re.match(r'^.*test.*.py$', file) is not None and not '__pycache__' in dir_name:
            newfile = TestFile(file, dir_name)
            test_files.append(newfile)

for file in test_files:
    print(file.get_full_name())
    print('-'*len(file.get_full_name()))
    for assertion in file.assertions:
        print(str(assertion.line_nr)+' - '+str(assertion.lines))
    print()
