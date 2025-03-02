# Generated by Django 5.1.6 on 2025-02-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a book'), ('can_change_book', 'Can edit a book'), ('can_delete_book', 'Can delete a book')]},
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
