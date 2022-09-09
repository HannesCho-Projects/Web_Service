# Generated by Django 4.1 on 2022-09-04 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0003_alter_house_baths_alter_house_bedrooms_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('accuracy', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('communication', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('cleanliness', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('location', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('check_in', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('value', models.PositiveIntegerField(verbose_name='default=1, validators = [MaxValueValidator(5), MinValueValidator(1)]')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='houses.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
