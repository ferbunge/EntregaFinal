# Generated by Django 4.0.5 on 2022-07-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cliente', models.CharField(max_length=50)),
                ('ape_cliente', models.CharField(max_length=50)),
                ('mail_cliente', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_proveedor', models.CharField(max_length=50)),
                ('mail_cliente', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='cantidad_art',
            new_name='cantidad',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='id_art',
        ),
    ]
