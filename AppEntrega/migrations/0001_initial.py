# Generated by Django 4.0.5 on 2022-07-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_art', models.IntegerField()),
                ('nom_art', models.CharField(max_length=50)),
                ('cantidad_art', models.IntegerField()),
            ],
        ),
    ]