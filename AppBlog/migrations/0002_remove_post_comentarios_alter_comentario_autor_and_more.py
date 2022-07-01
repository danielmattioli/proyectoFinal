# Generated by Django 4.0.4 on 2022-06-30 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentarios',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='AppBlog.post'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]