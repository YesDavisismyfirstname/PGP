# Generated by Django 2.2 on 2019-04-24 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_window', '0002_auto_20190423_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobbies',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lobbies',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lobby', to='game_window.Levels'),
        ),
        migrations.AlterField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player', to='game_window.Lobbies'),
        ),
        migrations.AlterField(
            model_name='player',
            name='riding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player', to='game_window.Poke_Rider'),
        ),
    ]
