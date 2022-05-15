import unittest
from utils import get_posts_by_tag


class TestGetPostsByTag(unittest.TestCase):
	def test_get_posts_by_tag(self):
		self.assertGreater(len(get_posts_by_tag('кот')), 0)
		self.assertEqual(type(get_posts_by_tag('кот')), list)


if __name__ == '__main__':
	unittest.main()
