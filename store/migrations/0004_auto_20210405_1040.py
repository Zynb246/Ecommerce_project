# Generated by Django 3.1.7 on 2021-04-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210402_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/image.png', upload_to='images/'),
        ),
    ]
