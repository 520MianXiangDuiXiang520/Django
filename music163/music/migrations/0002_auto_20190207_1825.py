# Generated by Django 2.1.4 on 2019-02-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='华语歌手',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('歌手姓名', models.CharField(max_length=50)),
                ('歌手ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='日本歌手',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('歌手姓名', models.CharField(max_length=50)),
                ('歌手ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='欧美歌手',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('歌手姓名', models.CharField(max_length=50)),
                ('歌手ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='韩国歌手',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('歌手姓名', models.CharField(max_length=50)),
                ('歌手ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='歌手',
            new_name='其他歌手',
        ),
    ]