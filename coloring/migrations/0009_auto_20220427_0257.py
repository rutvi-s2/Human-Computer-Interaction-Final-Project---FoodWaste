# Generated by Django 3.2.13 on 2022-04-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coloring', '0008_auto_20220425_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.CharField(default='bob', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='to_user',
            field=models.CharField(default='lisa', max_length=40),
            preserve_default=False,
        ),
    ]
