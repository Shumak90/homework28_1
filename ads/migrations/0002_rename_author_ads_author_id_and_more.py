# Generated by Django 4.0.6 on 2022-07-24 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='category',
            new_name='category_id',
        ),
    ]