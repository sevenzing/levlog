# Generated by Django 3.2.6 on 2022-01-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_emoji_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now=True, verbose_name='creation time'),
        ),
    ]
