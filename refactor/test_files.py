# Copyright (C) 2015  Gert Pellin
from refactor.lines import Line


class TestFile(object):
    def __init__(self, file_name, dir_name):
        self.file_name = file_name
        self.dir_name = dir_name
        self.lines = []
        f = open(self.get_full_name(), 'r')
        self.import_pytest = False
        for line in f:
            self.lines.append(Line(self, line))

    def get_full_name(self):
        return '{0}/{1}'.format(self.dir_name, self.file_name)

    def replace_file(self):
        """
        replace the original test-file with the pytest test-file
        """
        with open(self.get_full_name(), 'w') as file:
            for line in self.lines:
                if self.import_pytest and line.line[1] != '#':
                    file.write('import pytest\n')
                    self.import_pytest = False
                if line.assertion is not None:
                    file.write(line.get_refactor() + '\n')
                elif line.line:
                    file.write(line.line[:-1] + '\n')
