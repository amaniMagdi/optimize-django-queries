# Generated by Django 5.0.6 on 2024-06-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auther',
        ),
        migrations.AddField(
            model_name='post',
            name='authers',
            field=models.ManyToManyField(to='posts.auther'),
        ),
    ]
