# Generated by Django 4.2 on 2023-05-02 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_offre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
