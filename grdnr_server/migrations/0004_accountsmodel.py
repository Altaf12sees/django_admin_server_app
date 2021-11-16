# Generated by Django 3.2.6 on 2021-11-15 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grdnr_server', '0003_assigningjobsmodel_task_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(blank=True, max_length=100)),
                ('current_balance', models.CharField(max_length=10)),
                ('credit_amount', models.CharField(max_length=10)),
                ('debit_amount', models.CharField(max_length=10)),
                ('agent_account_status', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active'), ('Suspended', 'Suspended')], default='Active', max_length=50)),
                ('grdnr_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grdnr_server.grdnrsmodel')),
            ],
        ),
    ]