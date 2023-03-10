# Generated by Django 3.2.17 on 2023-02-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesupload',
            name='desc',
            field=models.TextField(default='SOME STRING', max_length=300),
        ),
        migrations.AddField(
            model_name='filesupload',
            name='image',
            field=models.ImageField(default='', upload_to='bookimage'),
        ),
        migrations.AddField(
            model_name='filesupload',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
