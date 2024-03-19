# Generated by Django 5.0.2 on 2024-03-19 12:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yournews', '0012_remove_comment_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='yournews.news'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
