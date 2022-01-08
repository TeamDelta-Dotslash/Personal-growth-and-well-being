# Generated by Django 4.0.1 on 2022-01-08 13:40

from django.db import migrations, models
import trackify.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('audio', models.FileField(upload_to='audio/%y', validators=[trackify.validators.file_size])),
            ],
        ),
    ]