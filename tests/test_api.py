import unittest
import requests


class TestApi(unittest.TestCase):
	def test_api_posts(self):
		response = requests.get('http://127.0.0.1:5000/api/posts').json()
		self.assertEqual(type(response), list)
		self.assertIn('pk', response[0])
		self.assertIn('poster_name', response[0])
		self.assertIn('content', response[0])

	def test_api_post_id(self):
		response = requests.get('http://127.0.0.1:5000/api/posts/2').json()
		self.assertEqual(type(response), dict)
		self.assertIn('pk', response)
		self.assertIn('poster_name', response)
		self.assertIn('content', response)


if __name__ == '__main__':
	unittest.main()
