# Generated by Django 2.0.13 on 2019-10-07 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20191007_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='ehGato',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='produto.Categoria'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='raca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='produto.Categoria'),
        ),
    ]
