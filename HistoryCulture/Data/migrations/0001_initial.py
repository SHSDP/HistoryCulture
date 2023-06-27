# Generated by Django 4.2.1 on 2023-06-03 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArhitectureObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('information', models.CharField(max_length=1000)),
                ('cor_x', models.FloatField()),
                ('cor_y', models.FloatField()),
                ('district', models.CharField(max_length=40)),
                ('town', models.CharField(max_length=40)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.arhitectureobject')),
            ],
        ),
        migrations.CreateModel(
            name='ArhitectureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('license', models.CharField(max_length=70)),
                ('url', models.CharField(max_length=200)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.arhitectureobject')),
            ],
        ),
    ]
