from django.test import TestCase
from stock.serializers import ArticleSerializer, TagSerializer, TweetTaskSerializer
from stock.models import Tag


class TagSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.tag_serializer = TagSerializer()

    def test_create(self):
        validated_data = {'name': 'python'}

        tag = self.tag_serializer.create(validated_data)
        tags = Tag.objects.all()
        self.assertEqual(tag.name, validated_data['name'])
        self.assertEqual(len(tags), 3)

    def test_create_duplicate(self):
        validated_data = {'name': 'maven'}

        tag = self.tag_serializer.create(validated_data)
        tags = Tag.objects.all()
        self.assertEqual(tag.name, validated_data['name'])
        self.assertEqual(len(tags), 2)


class ArticleSerializerTests(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.article_serializer = ArticleSerializer()
        self.tag_serializer = TagSerializer()

    def test_create(self):
        validated_data = {
            'title': 'Java応用',
            'url': 'http://localhost',
            'created_at': "2017-12-10T10:00:00+09:00",
            'tags': [{'name': 'maven'}, {'name': 'StreamingAPI'}]
        }
        self.tag_serializer.create(validated_data['tags'][0])
        self.tag_serializer.create(validated_data['tags'][1])

        article = self.article_serializer.create(validated_data)
        self.assertEqual(article.title, validated_data['title'])
        self.assertEqual(article.url, validated_data['url'])
        self.assertEqual(article.created_at, validated_data['created_at'])
        self.assertSetEqual(set([tag.name for tag in article.tags.all()]),
                            set([tag['name'] for tag in validated_data['tags']]))
        self.assertSetEqual(set([tag.name for tag in Tag.objects.all()]),
                            {'maven', 'SpringBoot', 'StreamingAPI'})


class TaskSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.task_serializer = TweetTaskSerializer()

    def test_create(self):
        validated_data = {'article_id': '00000000000000000000000000000000', 'title': 'Java基礎'}
        task = self.task_serializer.create(validated_data)
        self.assertEqual(task.article.title, validated_data['title'])
