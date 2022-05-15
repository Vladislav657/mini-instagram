import unittest
from utils import get_post_by_pk


class TestPostByPk(unittest.TestCase):
	def test_post_pk(self):
		self.assertEqual(get_post_by_pk(2)['poster_name'], "johnny")

	def test_not_post(self):
		self.assertEqual(get_post_by_pk(56), ValueError)


if __name__ == '__main__':
	unittest.main()
