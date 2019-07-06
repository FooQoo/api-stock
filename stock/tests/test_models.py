from django.test import TestCase
from stock.models import Article, Tag, TweetTask


class TagModelTests(TestCase):
    def test_create(self):
        tag = Tag()
        tag.name = "maven"
        tag.save()
        saved_tag = Tag.objects.all()
        self.assertEqual(saved_tag.count(), 1)
        self.assertEqual(saved_tag[0].name, "maven")


class ArticleModelTests(TestCase):
    def test_create(self):
        test_article = {
            'title': 'Java基礎',
            'url': 'http://localhost',
            'tags': [{'name': 'maven'}, {'name': 'SpringBoot'}],
        }
        article = Article.objects.create(
            title=test_article['title'],
            url=test_article['url']
        )
        article.save()
        tag1 = Tag.objects.create(name=test_article['tags'][0]['name'])
        article.tags.add(tag1)
        tag2 = Tag.objects.create(name=test_article['tags'][1]['name'])
        article.tags.add(tag2)
        article.save()

        saved_article = Article.objects.all()
        self.assertEqual(1, saved_article.count())
        self.assertEqual(test_article['title'], saved_article[0].title)
        self.assertEqual(test_article['url'], saved_article[0].url)
        actual_tags = {saved_article[0].tags.all()[0].name, saved_article[0].tags.all()[1].name}
        expected_tags = {test_article['tags'][0]['name'], test_article['tags'][1]['name']}
        self.assertSetEqual(expected_tags, actual_tags)


class TweetTaskModelTests(TestCase):
    def test_create(self):
        task = TweetTask()
        task.article = Article.objects.create(title='Java')
        task.save()

        saved_task = TweetTask.objects.all()
        self.assertEqual(1, saved_task.count())
        self.assertEqual(saved_task[0].status, 'waiting')
        self.assertEqual(saved_task[0].article.title, 'Java')

    def test_update(self):
        task = TweetTask()
        task.article = Article.objects.create(title='Java')
        task.save()

        article_id = TweetTask.objects.all()[0].article_id
        TweetTask.objects.update(status='processing')

        saved_task = TweetTask.objects.all()

        self.assertEqual(1, saved_task.count())
        self.assertEqual(saved_task[0].status, 'processing')
        self.assertEqual(saved_task[0].article.title, 'Java')