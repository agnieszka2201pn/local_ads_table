# Generated by Django 3.2.7 on 2021-09-22 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('content', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.IntegerField(choices=[(0, 'inne'), (1, 'odzież'), (2, 'motoryzacja'), (3, 'usługi'), (4, 'żywność')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user')),
            ],
        ),
    ]
