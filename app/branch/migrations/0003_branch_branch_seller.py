# Generated by Django 4.2.2 on 2023-07-15 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0002_branch_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
