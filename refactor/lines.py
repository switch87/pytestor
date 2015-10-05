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
            count_open = 0
            count_close = 0
            for letter in self.line:
                if letter == '(':
                    count_open += 1
                elif letter == ')':
                    count_close += 1

                # if 1-line assertion
            if count_open == count_close:
                self.assertion = Assertion([self.line])

            # todo: if multi-line assertion
            else:
                pass
