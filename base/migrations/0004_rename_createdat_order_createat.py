# Generated by Django 3.2.5 on 2021-08-10 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='createdAt',
            new_name='createAt',
        ),
    ]
