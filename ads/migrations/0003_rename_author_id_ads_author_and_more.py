# Generated by Django 4.0.6 on 2022-07-24 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_rename_author_ads_author_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='category_id',
            new_name='category',
        ),
    ]
