# Generated by Django 4.0.4 on 2022-06-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_alter_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='avatares/loginDefault.jpg', null=True, upload_to='avatares'),
        ),
    ]
