# Generated by Django 2.2.4 on 2019-08-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='category',
            field=models.CharField(choices=[('achado', 'achado'), ('perdido', 'perdido'), ('adoção', 'adoção')], default='achado', max_length=225),
        ),
    ]