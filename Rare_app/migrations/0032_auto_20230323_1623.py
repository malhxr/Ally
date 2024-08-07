# Generated by Django 3.2.6 on 2023-03-23 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rare_app', '0031_auto_20230322_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='paymet_info',
        ),
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Rare_app.orders'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='holder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_holder', to=settings.AUTH_USER_MODEL),
        ),
    ]
