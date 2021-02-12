# Generated by Django 3.1.6 on 2021-02-11 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='partner/')),
            ],
        ),
        migrations.CreateModel(
            name='ASD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_count', models.IntegerField(default=0)),
                ('url', models.URLField()),
                ('name', models.CharField(choices=[('YOUTUBE', 'YOUTUBE'), ('INSTAGRAM', 'INSTAGRAM'), ('TELEGRAM', 'TELEGRAM'), ('TIKTOK', 'TIKTOK')], max_length=150)),
                ('price', models.CharField(max_length=70)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partner.category')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.partner')),
            ],
        ),
    ]
