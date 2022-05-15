import unittest
from utils import get_posts_all, get_bookmarks_all


class TestGetJson(unittest.TestCase):
	def test_get_posts(self):
		self.assertEqual(type(get_posts_all()), list)

	def test_get_bookmarks(self):
		self.assertEqual(type(get_bookmarks_all()), list)


if __name__ == '__main__':
	unittest.main()
