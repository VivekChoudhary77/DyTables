# Generated by Django 3.1.1 on 2022-01-24 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0004_auto_20220124_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update_type', models.CharField(max_length=25)),
                ('row_data', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('table_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS.usertables')),
            ],
        ),
    ]
