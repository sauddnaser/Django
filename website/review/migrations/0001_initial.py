# Generated by Django 3.1 on 2023-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Email', models.CharField(max_length=255, null=True)),
                ('write', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
