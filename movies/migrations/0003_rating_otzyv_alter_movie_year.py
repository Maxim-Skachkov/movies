# Generated by Django 4.1.2 on 2022-10-31 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_commonfields_name_alter_person_born'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='otzyv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.review'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Год выхода фильма'),
        ),
    ]
