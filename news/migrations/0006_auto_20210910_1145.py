# Generated by Django 3.2.7 on 2021-09-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_news_item_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]