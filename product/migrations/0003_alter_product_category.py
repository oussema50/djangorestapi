# Generated by Django 3.2.24 on 2024-03-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20240229_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('phone', 'phone'), ('computer', 'computer'), ('television', 'television'), ('storage', 'storage')], max_length=50),
        ),
    ]
