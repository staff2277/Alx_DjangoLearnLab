# Generated by Django 5.1.6 on 2025-02-20 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_alter_author_name_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_app.author'),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relationship_app.library'),
        ),
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='relationship_app.book'),
        ),
    ]
