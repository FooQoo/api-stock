import uuid
from django.db import models


class Tag(models.Model):
    tag_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)


class Article(models.Model):
    article_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TweetTask(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    WAITING = "waiting"
    PROCESSING = "processing"
    FINISHED = "finished"
    STATUS_SET = (
        (WAITING, "待ち"),
        (PROCESSING, "処理中"),
        (FINISHED, "完了"),
    )
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS_SET, default=WAITING, max_length=10, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_id
