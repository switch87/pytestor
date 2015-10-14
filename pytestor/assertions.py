# Copyright (C) 2015  Gert Pellin
import re

from assertyon_type import assertion_types
from shared import bracket_compare


class Assertion(object):
    def __init__(self, line):
        self.line_object = line
        self.line = line.line
        self.line_nr = line.line_nr
        self.line_count = 1
        self.complete = False
        self.assertion_type = self.set_assertion_type()

    def get_line(self, line_nr):
        """
        returns 1 line of the assertion in pytest formatting.
        :param line_nr (int): The line number of the assertion to return
        :return: 1 line of the assertion (str)
        """
        return re.split(r'\n', self.line)[line_nr]

    def refactor(self):
        """
        refactor the assertion to pytest formatting, should only be ran after all lines of the assertion are present
        """
        if not self.assertion_type.keep_ending:
            self.line = self.line[:-2] + self.assertion_type.append
        if self.assertion_type.comma_replace is not None:
            comma_index = self.comma_finder()
            self.line = self.line[0:comma_index] + self.assertion_type.comma_replace + self.line[comma_index + 1:]
        self.line = self.line.replace(self.assertion_type.unittest, self.assertion_type.pytest)
        self.complete = True
        if self.assertion_type.import_pytest:
            self.line_object.file.import_pytest = True

    def set_assertion_type(self):
        """
        set the assertion type based on the formatting of the first line of the original assertion, assertion types
        are defined inside assertion_types
        :return: assertion type (AssertionType)
        """
        for assertion_type in assertion_types:
            if assertion_type.unittest in self.line:
                return assertion_type
        return None

    def comma_finder(self):
        """
        if necessary, find the comma relevant to the working of the assertion
        :return: index if the comma (int)
        """
        comma_index = self.line.find(',', 7)
        found = False
        counter = 0
        while not found and counter < 15:
            counter += 1
            count_single = 0
            count_double = 0
            for letter in self.line[7: comma_index]:
                if letter == "'":
                    count_single += 1
                if letter == '"':
                    count_double += 1
            if bracket_compare(self.line[re.match(r'.*self.assert.*\(', self.line).endpos + 1:comma_index]) and \
                    count_single % 2 == 0 and count_double % 2 == 0:
                found = True
            else:
                comma_index = self.line.find(',', comma_index + 1)
        return comma_index
