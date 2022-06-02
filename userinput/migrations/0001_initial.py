# Generated by Django 4.0.5 on 2022-06-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('chord1', models.CharField(choices=[('A', 'A'), ('A#', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#', 'C#/Db'), ('D', 'D'), ('D#', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#/Gb'), ('G', 'G'), ('G#', 'G#/Ab')], max_length=5)),
                ('chord1_bars', models.IntegerField()),
                ('chord2', models.CharField(choices=[('A', 'A'), ('A#', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#', 'C#/Db'), ('D', 'D'), ('D#', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#/Gb'), ('G', 'G'), ('G#', 'G#/Ab')], max_length=5)),
                ('chord2_bars', models.IntegerField()),
                ('chord3', models.CharField(choices=[('A', 'A'), ('A#', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#', 'C#/Db'), ('D', 'D'), ('D#', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#/Gb'), ('G', 'G'), ('G#', 'G#/Ab')], max_length=5)),
                ('chord3_bars', models.IntegerField()),
                ('chord4', models.CharField(choices=[('A', 'A'), ('A#', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#', 'C#/Db'), ('D', 'D'), ('D#', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#/Gb'), ('G', 'G'), ('G#', 'G#/Ab')], max_length=5)),
                ('chord4_bars', models.IntegerField()),
                ('chord5', models.CharField(choices=[('A', 'A'), ('A#', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#', 'C#/Db'), ('D', 'D'), ('D#', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#/Gb'), ('G', 'G'), ('G#', 'G#/Ab')], max_length=5)),
                ('chord5_bars', models.IntegerField()),
                ('midi', models.FileField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
    ]
