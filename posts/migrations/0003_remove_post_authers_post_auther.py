# Generated by Django 5.0.6 on 2024-06-25 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_auther_post_authers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='authers',
        ),
        migrations.AddField(
            model_name='post',
            name='auther',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.auther'),
        ),
    ]