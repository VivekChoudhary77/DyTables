# Generated by Django 3.1.1 on 2022-01-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('table_name', models.CharField(max_length=60, unique=b'I01\n')),
                ('table_schema', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]
