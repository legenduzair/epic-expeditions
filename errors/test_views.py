from django.test import TestCase


class TestErrors(TestCase):

    def test_page_not_found(self):

        response = self.client.get('/review_list/0/')
        self.assertEqual(response.status_code, 404)