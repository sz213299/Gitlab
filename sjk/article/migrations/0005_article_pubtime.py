# Generated by Django 3.2.19 on 2024-06-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20240603_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pubtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
