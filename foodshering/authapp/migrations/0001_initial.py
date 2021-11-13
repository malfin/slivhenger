# Generated by Django 3.2.9 on 2021-11-13 16:40

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('status', models.CharField(choices=[('v', 'Волонтёр'), ('c', 'Координатор')], default='v', max_length=1, verbose_name='Статус')),
                ('confirm', models.BooleanField(default=False, verbose_name='Подтверждён')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=128, verbose_name='Отчество')),
                ('city', models.CharField(max_length=128, verbose_name='Город')),
                ('address', models.CharField(max_length=128, verbose_name='Основной адрес (улица и дом)')),
                ('vk', models.URLField(verbose_name='Ссылка на страницу «ВКонтакте»')),
                ('phone', models.CharField(max_length=128, verbose_name='Номер телефона')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Анкета',
                'verbose_name_plural': 'Анкета',
            },
        ),
    ]
