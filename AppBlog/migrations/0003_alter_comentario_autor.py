# Generated by Django 4.0.4 on 2022-06-30 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_remove_post_comentarios_alter_comentario_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='AppBlog.post'),
            preserve_default=False,
        ),
    ]
