class AssertionType():

    def __init__(self, unittest, pytest='assert ', comma_replace=None, append='', keep_ending=False):
        self.unittest = unittest
        self.pytest = pytest
        self.comma_replace = comma_replace
        self.append = append
        self.keep_ending=keep_ending
