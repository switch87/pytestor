import re
from refactor.assertions import Assertion


class Line:
    def __init__(self, file, line):
        self.assertion = None
        self.file = file
        self.line_nr = len(file.lines)
        self.line = line
        self.set_assertions()


    def set_assertions(self, type=None):
        if 'self.assert' in self.line:
            # if 1-line assertion
            self.assertion = Assertion(self.line)

            # todo: if multi-line assertion
            if self.bracket_compare():
                self.assertion.refactor()
        else:
            if self.line_nr != 0:
                prevline = self.file.lines[self.line_nr-1]
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
                        self.line = None
                        self.assertion.linecount += 1
                        if self.bracket_compare():
                            self.assertion.refactor()

    def bracket_compare(self):
        count_open = 0
        count_close = 0
        for letter in self.assertion.line:
            if letter == '(':
                count_open += 1
            elif letter == ')':
                count_close += 1
        if count_close == count_open:
            return True
        else:
            return False
