# Generated by Django 3.2.5 on 2021-08-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210805_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testrun',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='testrun',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.testrun'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TestrunQuestion',
        ),
    ]
