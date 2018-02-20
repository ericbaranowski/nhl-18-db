# Generated by Django 2.0 on 2018-02-16 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0002_auto_20180214_1204'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skater',
            fields=[
                ('nhlcom_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('born', models.DateField()),
                ('number', models.IntegerField()),
                ('salary', models.FloatField()),
                ('years_left', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('draft_year', models.IntegerField(null=True)),
                ('draft_round', models.IntegerField(null=True)),
                ('draft_overall', models.IntegerField(null=True)),
                ('potential', models.IntegerField()),
                ('overall', models.IntegerField()),
                ('position', models.CharField(choices=[('c', 'Center'), ('d', 'Defenseman'), ('lw', 'Left Wing'), ('rw', 'Right Wing')], max_length=2)),
                ('type', models.CharField(choices=[('dfd', 'Defensive Defenseman'), ('grn', 'Grinder'), ('ofd', 'Offensive Defenseman'), ('ply', 'Playmaker'), ('pwf', 'Power Forward'), ('snp', 'Sniper'), ('twd', '2 Way Defender'), ('twf', '2 Way Forward')], max_length=3)),
                ('shoots', models.CharField(choices=[('l', 'Left'), ('r', 'Right')], max_length=1)),
                ('puck_skills', models.IntegerField()),
                ('senses', models.IntegerField()),
                ('shooting', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('skating', models.IntegerField()),
                ('physical', models.IntegerField()),
                ('deking', models.IntegerField()),
                ('hand_eye', models.IntegerField()),
                ('passing', models.IntegerField()),
                ('puck_control', models.IntegerField()),
                ('discipline', models.IntegerField()),
                ('offensive_awareness', models.IntegerField()),
                ('poise', models.IntegerField()),
                ('slap_shot_accuracy', models.IntegerField()),
                ('slap_shot_power', models.IntegerField()),
                ('wrist_shot_accuracy', models.IntegerField()),
                ('wrist_shot_power', models.IntegerField()),
                ('defensive_awareness', models.IntegerField()),
                ('faceoffs', models.IntegerField()),
                ('shot_blocking', models.IntegerField()),
                ('stick_checking', models.IntegerField()),
                ('acceleration', models.IntegerField()),
                ('agility', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('endurance', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('aggressiveness', models.IntegerField()),
                ('body_checking', models.IntegerField()),
                ('durability', models.IntegerField()),
                ('fighting_skill', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_skater', to='countries.Country')),
                ('draft_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players_skater_drafted', to='teams.Team')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_skater', to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]