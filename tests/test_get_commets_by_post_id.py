import unittest
from utils import get_comments_by_post_id


class TestGetCommentsByPostId(unittest.TestCase):
	def test_get_comments_by_post_id(self):
		post_id = get_comments_by_post_id(1)
		self.assertEqual(post_id[0]['comment'], "Очень здорово!")


if __name__ == '__main__':
	unittest.main()
