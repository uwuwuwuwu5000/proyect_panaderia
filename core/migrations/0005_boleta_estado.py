# Generated by Django 5.0.6 on 2024-06-26 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_stock_boleta_detalle_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('RE', 'Recibido'), ('NR', 'No Recibido'), ('PP', 'Procesando Pedido')], default='PP', max_length=2),
        ),
    ]
