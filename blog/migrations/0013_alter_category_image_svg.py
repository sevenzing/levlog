# Generated by Django 3.2.6 on 2021-08-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210825_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_svg',
            field=models.FileField(upload_to='category_images/', verbose_name='image'),
        ),
    ]
