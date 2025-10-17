# Testing
### Unittest package
```python
import unittest
from Sources.cap import just_do_it

class TestCap(unittest.TestCase):
    # Method is calling before each test
    def setUp(self):
        pass
    # Method is calling after each test
    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'duck'
        result = just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')


if __name__ == "__main__":
    unittest.main()
```
# Debugging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
- logging.debug('[DEBUG]')
- logging.info('[INFO]')
- logging.warn('[WARNING]')
- logging.error('[ERROR]')
- logging.critical('[CRITICAL]')
