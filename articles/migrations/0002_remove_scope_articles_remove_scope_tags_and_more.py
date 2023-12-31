# Generated by Django 4.1 on 2023-05-19 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='scope',
            name='tags',
        ),
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
            preserve_default=False,
        ),
    ]
