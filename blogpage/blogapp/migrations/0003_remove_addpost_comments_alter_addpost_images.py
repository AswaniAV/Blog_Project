# Generated by Django 5.1.2 on 2024-10-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_addpost_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpost',
            name='comments',
        ),
        migrations.AlterField(
            model_name='addpost',
            name='images',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
