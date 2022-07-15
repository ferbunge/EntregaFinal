# Generated by Django 4.0.5 on 2022-07-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0004_articulos_rename_cliente_clientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='articulos',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='ape',
        ),
    ]