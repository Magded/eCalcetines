# Generated by Django 2.2 on 2021-10-19 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32, verbose_name='Nombre')),
                ('imagen', models.CharField(max_length=32)),
                ('precio', models.FloatField()),
                ('cantidad_en_bodega', models.PositiveSmallIntegerField()),
                ('codigo', models.IntegerField(null=True)),
                ('oferta', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField(choices=[('EN PROCESO', 'EN PROCESO'), ('ENTREGADO', 'ENTREGADO'), ('PAGADO', 'PAGADO')])),
                ('usuario', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('delivery_type', models.TextField()),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Producto')),
            ],
        ),
    ]
