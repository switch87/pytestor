import fileinput
import re
from refactor.assertions import Assertion

__author__ = 'switch87'

class TestFile():

    def __init__(self, file_name, dir_name):
        self.file_name = file_name
        self.dir_name = dir_name
        self.assertions = []
        # create array from file content
        # with open(self.get_full_name()) as f:
        #   self.file_content = f.readlines()
        self.file_content = []
        f = open(self.get_full_name(),'r')
        for line in f:
            self.file_content.append(line)
        self.set_assertions()


    def get_full_name(self):
        return '{0}/{1}'.format(self.dir_name,self.file_name)

    def set_assertions(self, type=None):
        for line_nr, line in enumerate(self.file_content):
            if 'self.assert' in line:

                count_open = 0
                count_close = 0
                for letter in line:
                    if letter == '(':
                        count_open += 1
                    elif letter == ')':
                        count_close += 1

                    # if 1-line assertion
                if count_open == count_close:
                    self.assertions.append(Assertion(line_nr,[line[:-1]]))

                # todo: if multi-line assertion
                else:
                    pass
