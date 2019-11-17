# Generated by Django 2.2.6 on 2019-11-09 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0002_auto_20191109_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='container.BaseModel')),
                ('container_number', models.CharField(max_length=255)),
            ],
            bases=('container.basemodel',),
        ),
        migrations.CreateModel(
            name='PakistaniPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('duty_tax', models.IntegerField(blank=True, null=True)),
                ('other_charges', models.IntegerField(blank=True, null=True)),
                ('total_paid', models.IntegerField(blank=True, null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='container.Container')),
            ],
        ),
        migrations.CreateModel(
            name='ChinaPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tt_amount', models.FloatField(blank=True, null=True)),
                ('tt_charges', models.FloatField(blank=True, null=True)),
                ('rmb_comission', models.FloatField(blank=True, null=True)),
                ('total_paid', models.FloatField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='container.Container')),
            ],
        ),
    ]
