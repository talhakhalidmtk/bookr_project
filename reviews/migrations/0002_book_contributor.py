# Generated by Django 4.1.7 on 2023-02-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the book.', max_length=70)),
                ('publication_date', models.DateField(verbose_name='Date the book was published.')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number of the book.')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(help_text="The contributor's first name or names.", max_length=50)),
                ('last_names', models.CharField(help_text="The contributor's last name or names.", max_length=50)),
                ('email', models.EmailField(help_text='The contact email for the contributor.', max_length=254)),
            ],
        ),
    ]
