# Generated by Django 4.2 on 2023-10-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_question_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
