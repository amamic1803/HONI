import os
import unittest
from tests.test_honi.utils import HoniTest
import honi.year2022.round5.macak as script


class TestScript(HoniTest):
    def test_script(self):
        self.run_io_tests(script, os.path.join(os.path.dirname(__file__), "test-data", "macak"))


if __name__ == '__main__':
    unittest.main()
