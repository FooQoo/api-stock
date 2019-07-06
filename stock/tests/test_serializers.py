from django.test import TestCase
from stock.serializers import ArticleSerializer
from stock.models import Tag, TweetTask


class TagModelTests(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.serializer = ArticleSerializer()

    def test_create(self):
        validated_data = {
            'title': 'Java応用',
            'url': 'http://localhost',
            'created_at': "2017-12-10T10:00:00+09:00",
            'tags': [{'name': 'maven'}, {'name': 'StreamingAPI'}]
        }

        article = self.serializer.create(validated_data)
        self.assertEqual(article.title, validated_data['title'])
        self.assertEqual(article.url, validated_data['url'])
        self.assertEqual(article.created_at, validated_data['created_at'])
        self.assertSetEqual(set([tag.name for tag in article.tags.all()]),
                            set([tag['name'] for tag in validated_data['tags']]))
        self.assertSetEqual(set([tag.name for tag in Tag.objects.all()]),
                            {'maven', 'SpringBoot', 'StreamingAPI'})
        self.assertSetEqual(set([task.article.title for task in TweetTask.objects.all()]),
                            {'Java基礎', 'Java応用'})
