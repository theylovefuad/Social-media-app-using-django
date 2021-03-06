# Generated by Django 4.0.5 on 2022-06-26 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0006_rename_comment_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('picture', models.ImageField(blank=True, default='default_user.jpg', upload_to='post_photos')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
