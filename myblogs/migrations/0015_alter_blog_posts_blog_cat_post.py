# Generated by Django 5.0.1 on 2024-01-29 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0014_rename_blog_cat_blog_posts_blog_cat_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_posts',
            name='blog_cat_post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_category'),
        ),
    ]
