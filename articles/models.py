from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    # related_name='articles'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(default=False, max_length=500)
    text = models.TextField(default=False)
    image = models.ImageField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope')

    def __str__(self):
        return self.title


class Scope(models.Model):
    is_main = models.BooleanField(default=False)                    # Один параметр определения - главный тег или не главный
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')



