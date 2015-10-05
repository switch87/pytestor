import fileinput
import re
from refactor.assertions import Assertion
from refactor.lines import Line

__author__ = 'switch87'

class TestFile():

    def __init__(self, file_name, dir_name):
        self.file_name = file_name
        self.dir_name = dir_name
        self.lines = []
        f = open(self.get_full_name(),'r')
        for line in f:
            self.lines.append(Line(self, line[:-1]))

    def get_full_name(self):
        return '{0}/{1}'.format(self.dir_name,self.file_name)

    def replace_file(self):
        with open(self.get_full_name(),'w') as file:
            for line in self.lines:
                if line.assertion is not None:
                    file.write(line.assertion.lines[0]+'\n')
                else:
                    file.write(line.line+'\n')