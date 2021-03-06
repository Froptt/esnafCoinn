# Generated by Django 3.2.4 on 2021-06-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=50, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(max_length=200, verbose_name='Yorum'),
        ),
    ]
