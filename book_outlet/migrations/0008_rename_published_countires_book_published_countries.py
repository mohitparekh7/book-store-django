# Generated by Django 3.2.4 on 2021-07-04 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_auto_20210705_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_countires',
            new_name='published_countries',
        ),
    ]