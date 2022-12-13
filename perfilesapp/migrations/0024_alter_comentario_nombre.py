# Generated by Django 4.0.5 on 2022-07-24 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfilesapp', '0023_alter_comentario_comentario_alter_comentario_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
