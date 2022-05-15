import unittest
from utils import get_posts_by_user


class TestGetPostByUser(unittest.TestCase):
	def test_user_posts(self):
		data = get_posts_by_user('Johnny')
		self.assertGreater(len(data), 1)
		self.assertIn('pk', data[0])


if __name__ == '__main__':
	unittest.main()
