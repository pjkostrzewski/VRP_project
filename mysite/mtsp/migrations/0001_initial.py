# Generated by Django 3.0.3 on 2020-03-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]
