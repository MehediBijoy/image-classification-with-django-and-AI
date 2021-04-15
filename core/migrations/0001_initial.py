# Generated by Django 3.2 on 2021-04-15 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='classifiedCharacters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='imageExtractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False)),
                ('voted', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='imageWithCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classifiedcharacters')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.imageextractor')),
            ],
        ),
        migrations.CreateModel(
            name='classifiedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(default=0)),
                ('classified_char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classifiedcharacters')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.imageextractor')),
            ],
        ),
    ]
