# Generated by Django 3.1 on 2023-12-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startingwebsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tea',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tea',
            name='body',
        ),
        migrations.RemoveField(
            model_name='tea',
            name='title',
        ),
        migrations.AddField(
            model_name='tea',
            name='Country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tea',
            name='Grade',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tea',
            name='Images',
            field=models.ImageField(null=True, upload_to='Tea_images/'),
        ),
        migrations.AddField(
            model_name='tea',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
