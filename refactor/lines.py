# Copyright (C) 2015  Gert Pellin
import re
from refactor.assertions import Assertion
from refactor.shared import bracket_compare


class Line(object):
    def __init__(self, file, line):
        self.assertion = None
        self.file = file
        self.line_nr = len(file.lines)
        self.line = line
        self.set_assertions()

    def set_assertions(self):
        """
        set the pytest assertion for the line, returns None if no assertion is present
        """
        if 'self.assert' in self.line:
            self.assertion = Assertion(self)
            if self.assertion.assertion_type is None:
                self.assertion = None
                return

            if bracket_compare(self.assertion.line) and self.assertion.line[-2] != ',':
                self.assertion.refactor()
        else:
            if self.line_nr != 0:
                prevline = self.file.lines[self.line_nr - 1]
                if prevline.assertion is not None:
                    if not prevline.assertion.complete:
                        self.assertion = prevline.assertion

                        backslash = True
                        brackets = re.findall(r'[()]', self.assertion.line)
                        if brackets is not None:
                            if (brackets[-1] == '(' and len(brackets) >= 2) \
                                    or self.assertion.assertion_type.pytest[-1] == '(':
                                backslash = False
                            else:
                                backslash = True
                        if backslash:
                            self.assertion.line = self.assertion.line[:-1] + '\\\n' + self.line
                        else:
                            self.assertion.line = self.assertion.line + self.line
                        self.assertion.line_count += 1
                        if bracket_compare(self.assertion.line):
                            self.assertion.refactor()

    def get_refactor(self):
        """
        return the line in pytest formatting if available, else it returns the original line
        :return: line (str)
        """
        if self.assertion:
            return self.assertion.get_line(self.line_nr - self.assertion.line_nr)
        return self.get_original()

    def get_original(self):
        return self.line
