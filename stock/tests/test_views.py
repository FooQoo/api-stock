import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from urllib.parse import urlencode


class ArticleViewTests(APITestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        pass

    def test_create(self):
        payload = {
            'title': 'Java応用',
            'url': 'http://localhost',
            'created_at': "2017-12-10T10:00:00+09:00",
            'tags': [{'name': 'maven'}, {'name': 'StreamingAPI'}],
        }
        url = reverse("article-list")
        response = self.client.post(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TweetTaskViewTests(APITestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        pass

    def test_get(self):
        query = urlencode({'status': 'waiting', 'ordering': 'updated_at', 'limit': 1})
        url = reverse("tweettask-list") + '?' + query
        response = self.client.get(url, format='json')
        results = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(results))
