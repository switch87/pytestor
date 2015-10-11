class AssertionType():
    def __init__(self, unittest, pytest='assert ', comma_replace=None, append='', keep_ending=False, import_pytest=False):
        self.unittest = unittest
        self.pytest = pytest
        self.comma_replace = comma_replace
        self.append = append
        self.keep_ending=keep_ending
        self.import_pytest = import_pytest

assertion_types = [
    AssertionType(unittest='self.assertEqual(', comma_replace=' =='),
    AssertionType(unittest='self.assertGreater(', comma_replace=' >'),
    AssertionType(unittest='self.assertGreaterEqual(', comma_replace=' >='),
    AssertionType(unittest='self.assertLess(', comma_replace=' <'),
    AssertionType(unittest='self.assertLessEqual(', comma_replace=' <='),
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
    AssertionType(unittest='self.assertRaises(', pytest='pytest.raises(', keep_ending=True, import_pytest=True),

    AssertionType(unittest='self.assertCreates(', pytest='self.assertCreates(', keep_ending=True),
    AssertionType(unittest='self.assertCount(', pytest='self.assertCount(', keep_ending=True)
]
