# Generated by Django 3.0.3 on 2020-02-15 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('release_date', models.TimeField()),
                ('parentListID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toDoList.Listas')),
            ],
        ),
        migrations.AddField(
            model_name='listas',
            name='parentUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toDoList.Usuarios'),
        ),
    ]
