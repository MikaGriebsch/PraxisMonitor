# Generated by Django 5.1.7 on 2025-03-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_alter_patient_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('absend', 'Abwehsend'), ('waiting', 'Wartend'), ('room1', 'Raum 1'), ('room2', 'Raum 2'), ('done', 'Fertig')], default='waiting', max_length=20),
        ),
    ]
