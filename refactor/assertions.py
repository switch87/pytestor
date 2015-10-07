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
        AssertionType(unittest='self.assertIsInstance', pytest='assert isinstance', keep_ending=True),
        AssertionType(unittest='self.assertIsNone', append=' is None'),
        AssertionType(unittest='self.assertIsNotNone', append=' is not None'),
        AssertionType(unittest='self.assertRaises(', pytest='pytest.raises(', keep_ending=True)
    ]

    def __init__(self, line):
        self.line = line
        self.linecount = 1
        self.complete = False
        self.assertion_type = self.set_assertion_type()

    def refactor(self):

        self.line = self.line.replace(self.assertion_type.unittest, self.assertion_type.pytest)
        if not self.assertion_type.keep_ending:
            self.line = self.line[:-1] + self.assertion_type.append
        if self.assertion_type.comma_replace is not None:
            comma_index = self.comma_finder()
            self.line = self.line[0:comma_index]+' =='+self.line[comma_index+1:]
        self.complete = True

    def set_assertion_type(self):

        for assertion_type in self.assertion_types:
            if assertion_type.unittest in self.line:
                return assertion_type
        return self.assertion_types[0]

    def comma_finder(self):

        comma_index = self.line.find(',', 7)
        found = False
        counter = 0
        while not found and counter < 15:
            counter += 1
            count_open = 0
            count_close = 0
            count_single = 0
            count_double = 0
            for letter in self.line[7: comma_index]:
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
                comma_index = self.line.find(',',comma_index+1)
        return comma_index
