# Generated by Django 3.2.6 on 2021-11-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_category_image_svg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='emoji_description',
            field=models.CharField(max_length=256, null=True, verbose_name='emoji'),
        ),
    ]