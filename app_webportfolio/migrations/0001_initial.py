# Generated by Django 4.2.7 on 2023-11-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='desempeno',
            fields=[
                ('pk_desempeno', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='educacion',
            fields=[
                ('pk_educacion', models.AutoField(primary_key=True, serialize=False)),
                ('establecimiento', models.CharField(max_length=150, verbose_name='establecimiento donde se obtuvo')),
                ('titulo', models.CharField(max_length=150, verbose_name='titulo conseguido')),
                ('descripcion', models.TextField(verbose_name='desempeño del titulo')),
                ('promedio', models.IntegerField(verbose_name='Mi promedio obtenido')),
                ('fecha_inicio', models.DateField(verbose_name='fecha de inicio preparacion academica')),
                ('fecha_salida', models.DateField(verbose_name='fecha de finalizacion preparacion academica')),
            ],
        ),
        migrations.CreateModel(
            name='experiencia',
            fields=[
                ('pk_experiencia', models.AutoField(primary_key=True, serialize=False)),
                ('puesto', models.CharField(max_length=150, verbose_name='puesto funcional')),
                ('empresa', models.CharField(max_length=150, verbose_name='empresa donde trabaje')),
                ('descripcion', models.TextField(verbose_name='desempeño dentro de la empresa')),
                ('fecha_inicio', models.DateField(verbose_name='fecha de inicio laboral')),
                ('fecha_salida', models.DateField(verbose_name='fecha de finalizacion laboral')),
            ],
        ),
        migrations.CreateModel(
            name='icono',
            fields=[
                ('pk_icono', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre icono')),
                ('estructura', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='interes',
            fields=[
                ('pk_interes', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='reconocimiento',
            fields=[
                ('pk_reconocimiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='sobremi',
            fields=[
                ('pk_sobremi', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='mi nombre')),
                ('direccion', models.CharField(max_length=300, verbose_name='mi direccion')),
                ('telefono', models.CharField(max_length=8, verbose_name='telefono de contacto')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo de contacto')),
                ('descripcion', models.TextField(verbose_name='Breve descripcion de mi persona')),
                ('foto', models.URLField(verbose_name='Foto de mi persona')),
            ],
        ),
    ]
