# Generated by Django 3.1.5 on 2021-06-13 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAssesments1',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200, null=True)),
                ('problem', models.TextField(null=True)),
                ('des', models.TextField(null=True)),
                ('marks', models.IntegerField(default=0, null=True)),
                ('flag', models.CharField(default='D', editable=False, max_length=1)),
                ('category', models.CharField(choices=[('SEEKER(LEVEL 1)', 'SEEKER(LEVEL 1)'), ('PRACTITIONER(LEVEL 2)', 'PRACTITIONER(LEVEL 2)'), ('CHALLENGER(LEVEL 3)', 'CHALLENGER(LEVEL 3)'), ('PERFORMER(LEVEL 4)', 'PERFORMER(LEVEL 4)')], max_length=200, null=True)),
                ('inp1', models.TextField(blank=True, null=True)),
                ('outp1', models.TextField(blank=True, null=True)),
                ('inp2', models.TextField(blank=True, null=True)),
                ('outp2', models.TextField(blank=True, null=True)),
                ('max_marks', models.IntegerField(default=0)),
                ('tcs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyAssesments',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200, null=True)),
                ('problem', models.TextField(null=True)),
                ('des', models.TextField(null=True)),
                ('marks', models.IntegerField()),
                ('flag', models.CharField(default='M', editable=False, max_length=1)),
                ('category', models.CharField(choices=[('SEEKER(LEVEL 1)', 'SEEKER(LEVEL 1)'), ('PRACTITIONER(LEVEL 2)', 'PRACTITIONER(LEVEL 2)'), ('CHALLENGER(LEVEL 3)', 'CHALLENGER(LEVEL 3)'), ('PERFORMER(LEVEL 4)', 'PERFORMER(LEVEL 4)')], max_length=200, null=True)),
                ('inp1', models.TextField(blank=True, null=True)),
                ('outp1', models.TextField(blank=True, null=True)),
                ('inp2', models.TextField(blank=True, null=True)),
                ('outp2', models.TextField(blank=True, null=True)),
                ('max_marks', models.IntegerField(default=0)),
                ('tcs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('yearOfStudy', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=5, null=True)),
                ('category', models.CharField(choices=[('SEEKER(LEVEL 1)', 'SEEKER(LEVEL 1)'), ('PRACTITIONER(LEVEL 2)', 'PRACTITIONER(LEVEL 2)'), ('CHALLENGER(LEVEL 3)', 'CHALLENGER(LEVEL 3)'), ('PERFORMER(LEVEL 4)', 'PERFORMER(LEVEL 4)')], max_length=200, null=True)),
                ('total_marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyAssesments',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200, null=True)),
                ('problem', models.TextField(null=True)),
                ('des', models.TextField(null=True)),
                ('marks', models.IntegerField()),
                ('flag', models.CharField(default='W', editable=False, max_length=1)),
                ('category', models.CharField(choices=[('SEEKER(LEVEL 1)', 'SEEKER(LEVEL 1)'), ('PRACTITIONER(LEVEL 2)', 'PRACTITIONER(LEVEL 2)'), ('CHALLENGER(LEVEL 3)', 'CHALLENGER(LEVEL 3)'), ('PERFORMER(LEVEL 4)', 'PERFORMER(LEVEL 4)')], max_length=200, null=True)),
                ('inp1', models.TextField(blank=True, null=True)),
                ('outp1', models.TextField(blank=True, null=True)),
                ('inp2', models.TextField(blank=True, null=True)),
                ('outp2', models.TextField(blank=True, null=True)),
                ('max_marks', models.IntegerField(default=0)),
                ('tcs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmarks', models.IntegerField(default=0)),
                ('mmarks', models.IntegerField(default=0)),
                ('wmarks', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('SEEKER(LEVEL 1)', 'SEEKER(LEVEL 1)'), ('PRACTITIONER(LEVEL 2)', 'PRACTITIONER(LEVEL 2)'), ('CHALLENGER(LEVEL 3)', 'CHALLENGER(LEVEL 3)'), ('PERFORMER(LEVEL 4)', 'PERFORMER(LEVEL 4)')], max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionForum',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competitive_coding_club.discussionforum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='clinks',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('frmassessment', models.CharField(max_length=1, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, choices=[('cpp', 'cpp'), ('c', 'c'), ('cs', 'cs'), ('java', 'java'), ('py', 'py'), ('rb', 'rb'), ('kt', 'kt'), ('kt', 'kt'), ('swift', 'swift')], max_length=5, null=True)),
                ('marks', models.IntegerField(default=0)),
                ('problem', models.TextField(blank=True, null=True)),
                ('heading', models.CharField(blank=True, max_length=200, null=True)),
                ('sub', models.IntegerField(default=0)),
                ('subfail', models.IntegerField(default=0)),
                ('dpid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitive_coding_club.dailyassesments1')),
                ('mpid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitive_coding_club.monthlyassesments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wpid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitive_coding_club.weeklyassesments')),
            ],
        ),
    ]
