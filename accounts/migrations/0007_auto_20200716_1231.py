# Generated by Django 2.2.8 on 2020-07-16 11:31

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200715_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='course',
            field=models.CharField(max_length=50, verbose_name='Discipline'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pix',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile picture'),
        ),
        migrations.CreateModel(
            name='SubSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_skill', models.CharField(max_length=30)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('in_progress', models.BinaryField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]