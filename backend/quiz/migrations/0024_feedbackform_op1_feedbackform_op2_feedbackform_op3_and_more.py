# Generated by Django 4.2.2 on 2024-02-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0023_alter_feedbackform_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackform',
            name='op1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='op2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='op3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='op4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='op5',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
