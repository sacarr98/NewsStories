# Generated by Django 4.2.7 on 2024-03-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yournews', '0019_news_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
