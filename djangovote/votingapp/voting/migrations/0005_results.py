# Generated by Django 2.0.7 on 2018-09-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20180908_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker1', models.IntegerField()),
                ('speaker2', models.IntegerField()),
                ('speaker3', models.IntegerField()),
                ('speaker4', models.IntegerField()),
                ('evalu1', models.IntegerField()),
                ('evalu2', models.IntegerField()),
                ('evalu3', models.IntegerField()),
                ('evalu4', models.IntegerField()),
                ('table1', models.IntegerField()),
                ('table2', models.IntegerField()),
                ('table3', models.IntegerField()),
                ('table4', models.IntegerField()),
                ('table5', models.IntegerField()),
                ('table6', models.IntegerField()),
                ('table7', models.IntegerField()),
            ],
        ),
    ]
