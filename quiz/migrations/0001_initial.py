"""
Quiz app uchun initial migration.

MUHIM: Bu migration 'fake' sifatida bajarilishi kerak, chunki jadvallar
allaqachon 'javohir' app migratsiyasi orqali yaratilgan.

Buyruq:
    python manage.py migrate quiz --fake-initial
"""
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=500, verbose_name='Iqtibos matni')),
                ('muallif', models.CharField(max_length=200, verbose_name='Muallif')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Yaratilgan vaqt')),
            ],
            options={
                'verbose_name': 'Iqtibos',
                'verbose_name_plural': 'Iqtiboslar',
                'db_table': 'javohir_bitik',
            },
        ),
        migrations.CreateModel(
            name='Sinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Sinf nomi')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    verbose_name='Yangilangan vaqt')),
            ],
            options={
                'verbose_name': 'Sinf',
                'verbose_name_plural': 'Sinflar',
                'ordering': ['nom'],
                'db_table': 'javohir_sinf',
            },
        ),
        migrations.CreateModel(
            name='Savol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('savol', models.CharField(max_length=500, verbose_name='Savol matni')),
                ('variant1', models.CharField(max_length=200, verbose_name='Variant A')),
                ('variant2', models.CharField(max_length=200, verbose_name='Variant B')),
                ('variant3', models.CharField(max_length=200, verbose_name='Variant C')),
                ('tjavob', models.CharField(
                    max_length=1,
                    choices=[('1', 'Variant A'), ('2', 'Variant B'), ('3', 'Variant C')],
                    verbose_name="To'g'ri javob",
                )),
                ('image', models.ImageField(blank=True, null=True, upload_to='',
                                             verbose_name='Rasm')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    verbose_name='Yangilangan vaqt')),
                ('sinf', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.RESTRICT,
                    to='quiz.sinf',
                    verbose_name='Sinf',
                )),
            ],
            options={
                'verbose_name': 'Savol',
                'verbose_name_plural': 'Savollar',
                'db_table': 'javohir_savol',
            },
        ),
        migrations.CreateModel(
            name='Natija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('tjavob', models.IntegerField(verbose_name="To'g'ri javoblar")),
                ('njavob', models.IntegerField(verbose_name="Noto'g'ri javoblar")),
                ('jamisavol', models.IntegerField(verbose_name='Jami savollar')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Foydalanuvchi',
                )),
                ('sinf', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='quiz.sinf',
                    verbose_name='Sinf',
                )),
            ],
            options={
                'verbose_name': 'Natija',
                'verbose_name_plural': 'Natijalar',
                'ordering': ['-date'],
                'db_table': 'javohir_natija',
            },
        ),
    ]
