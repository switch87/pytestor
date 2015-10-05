from refactor.assertyon_type import AssertionType


class Assertion():

    assertion_types = [
        AssertionType(unittest='self.assertEqual(', comma_replace=' =='),
        AssertionType(unittest='self.assertEquals(', comma_replace=' =='),
        AssertionType(unittest='self.assertListEqual(', comma_replace=' =='),
        AssertionType(unittest='self.assertNotEqual(', comma_replace=' !='),
        AssertionType(unittest='self.assertIn(', comma_replace=' in'),
        AssertionType(unittest='self.assertNotIn(', comma_replace=' not in'),
        AssertionType(unittest='self.assertTrue('),
        AssertionType(unittest='self.assertFalse(', pytest='assert not '),
        AssertionType(unittest='self.assertIsInstance', pytest='assert isinstance'),
        AssertionType(unittest='self.assertIsNone', append=' is None'),
        AssertionType(unittest='self.assertIsNotNone', append=' is not None')
    ]

    def __init__(self, line_nr, lines):
        self.line_nr = line_nr
        self.lines = lines
        self.refactor()

    def refactor(self):
        #assertTrue
        for assertion_type in self.assertion_types:
            if assertion_type.unittest in self.lines[0]:
                self.lines[0] = self.lines[0].replace(assertion_type.unittest, assertion_type.pytest)
                self.lines[-1] = self.lines[-1][:-1] + assertion_type.append
                if assertion_type.comma_replace is not None:
                    comma_index = self.comma_finder()
                    self.lines[0] = self.lines[0][0:comma_index]+' =='+self.lines[0][comma_index+1:]

    def comma_finder(self):

        comma_index = self.lines[0].find(',', 7)
        found = False
        counter = 0
        while not found and counter < 15:
            counter += 1
            count_open = 0
            count_close = 0
            count_single = 0
            count_double = 0
            for letter in self.lines[0][7: comma_index]:
                if letter == '(':
                    count_open += 1
                elif letter == ')':
                    count_close += 1
                elif letter == "'":
                    count_single += 1
                elif letter == '"':
                    count_double += 1
            if count_close == count_open and \
                                    count_single%2 == 0 and \
                                    count_double%2 == 0:
                found = True
            else:
                comma_index = self.lines[0].find(',',comma_index+1)
        return comma_index
