# Generated by Django 4.1.2 on 2023-01-31 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0021_remove_article_liked_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comm_user_like',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
