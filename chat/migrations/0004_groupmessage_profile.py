# Generated by Django 4.2.17 on 2024-12-31 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('chat', '0003_remove_chatgroup_users_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_messages', to='account.profile'),
        ),
    ]
