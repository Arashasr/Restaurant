# Generated by Django 3.2 on 2022-05-20 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('created_at',)},
        ),
    ]