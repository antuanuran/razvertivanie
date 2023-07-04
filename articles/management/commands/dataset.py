import csv
from datetime import datetime

from django.core.management import BaseCommand
from django.utils.text import slugify
from articles.models import Tag, Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('dataset.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phon in phones:
            Tag.objects.create(name=phon['color'])
            phon = Article.objects.create(title=phon['title'], text=phon['text'], image=phon['image'])
            phon.tags.add(Tag.objects.first())











