# Generated by Django 4.1.4 on 2023-11-18 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
        ('accounts', '0003_alter_student_field_of_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='field_of_study',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_field_of_study', to='college.fieldofstudy'),
        ),
        migrations.AlterField(
            model_name='student',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_supervisor', to='accounts.professor'),
        ),
    ]
