import unittest
from utils import search_for_posts


class TestSearchForPosts(unittest.TestCase):
	def test_query_posts(self):
		data = search_for_posts('ПиРог')
		self.assertEqual(data[0]['pk'], 1)


if __name__ == '__main__':
	unittest.main()
