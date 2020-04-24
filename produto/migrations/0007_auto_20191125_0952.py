# Generated by Django 2.0.13 on 2019-11-25 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0006_auto_20191011_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gato',
            name='raca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='produto.Raca'),
        ),
    ]