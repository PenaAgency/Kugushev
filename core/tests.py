from rest_framework.test import APITestCase
from .tasks import update_db


class Tests(APITestCase):

    def test_posts(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_celery(self):
        self.assertEqual(update_db().get('result'), 'Success')
