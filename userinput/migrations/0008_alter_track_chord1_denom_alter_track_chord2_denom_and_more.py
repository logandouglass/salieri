# Generated by Django 4.0.4 on 2022-06-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0007_alter_composition_chord1_bars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='chord1_denom',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='track',
            name='chord2_denom',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='track',
            name='chord3_denom',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='track',
            name='chord4_denom',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='track',
            name='chord5_denom',
            field=models.IntegerField(default=4),
        ),
    ]
