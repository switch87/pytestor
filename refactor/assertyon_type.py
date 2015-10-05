class AssertionType():

    def __init__(self, unittest, pytest='assert ', comma_replace=None, append=''):
        self.unittest = unittest
        self.pytest = pytest
        self.comma_replace = comma_replace
        self.append = append
