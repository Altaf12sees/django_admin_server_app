# Generated by Django 3.2.6 on 2021-10-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grdnr_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigningjobsmodel',
            name='grdnr_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grdnr_server.grdnrsmodel'),
        ),
        migrations.AddField(
            model_name='assigningjobsmodel',
            name='task_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grdnr_server.taskmodel'),
        ),
    ]