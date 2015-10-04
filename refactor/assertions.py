class Assertion():
    def __init__(self, line_nr, lines):
        self.line_nr = line_nr
        self.lines = lines
        self.refactor()

    def refactor(self):
        #assertTrue
        if 'self.assertTrue(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertTrue(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
        elif 'self.assertFalse(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertFalse(', 'assert not ')
            self.lines[-1] = self.lines[-1][:-1]
        elif 'self.assertIsInstance(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertIsInstance(', 'assert isinstance(')
        elif 'self.assertIsNone(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertIsNone(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]+' is None'
        elif 'self.assertIsNotNone(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertIsNotNone(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]+' is not None'

        # todo: will not work for multi-line
        if 'self.assertIn(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertIn(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
            comma_index = self.comma_finder()
            self.lines[0] = self.lines[0][0:comma_index-1]+' in'+self.lines[0][comma_index+1:]

        # todo: will not work for multi-line
        if 'self.assertEqual(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertEqual(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
            comma_index = self.comma_finder()
            self.lines[0] = self.lines[0][0:comma_index]+' =='+self.lines[0][comma_index+1:]
        # todo: will not work for multi-line
        if 'self.assertEquals(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertEquals(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
            comma_index = self.comma_finder()
            self.lines[0] = self.lines[0][0:comma_index]+' =='+self.lines[0][comma_index+1:]
        # todo: will not work for multi-line
        if 'self.assertListEquals(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertListEquals(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
            comma_index = self.comma_finder()
            self.lines[0] = self.lines[0][0:comma_index]+' =='+self.lines[0][comma_index+1:]

        # todo: will not work for multi-line
        if 'self.assertNotEqual(' in self.lines[0]:
            self.lines[0] = self.lines[0].replace('self.assertNotEqual(', 'assert ')
            self.lines[-1] = self.lines[-1][:-1]
            comma_index = self.comma_finder()
            self.lines[0] = self.lines[0][0:comma_index]+' !='+self.lines[0][comma_index+1:]

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
