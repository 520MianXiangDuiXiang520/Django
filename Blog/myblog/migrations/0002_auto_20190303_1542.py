# Generated by Django 2.1.4 on 2019-03-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='文章内容',
            name='标题',
            field=models.CharField(max_length=30),
        ),
    ]
