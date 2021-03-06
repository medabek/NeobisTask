# Generated by Django 2.1.2 on 2018-10-14 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=300)),
                ('longitude', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('imgpath', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_choice', models.IntegerField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')])),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1500)),
                ('logo', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='course.Category')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='contacts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='course.Course'),
        ),
        migrations.AddField(
            model_name='branch',
            name='branches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='course.Course'),
        ),
    ]
