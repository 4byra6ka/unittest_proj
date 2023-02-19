import unittest
from utils import dicts

class TestDicts(unittest.TestCase):
    """Unittest на основе TDD"""
    def test_get_val(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), "mercurial")
        self.assertEqual(dicts.get_val({}, "vcs", "git"), "git")
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")
        self.assertEqual(dicts.get_val({"vcs1": "mercurial1", }, "vcs", "bazaar"), "bazaar")
        self.assertEqual(dicts.get_val({"vcs1": "mercurial1", "vcs": "mercurial"}, "vcs", "bazaar"), "mercurial")