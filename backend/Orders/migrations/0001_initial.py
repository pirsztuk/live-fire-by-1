# Generated by Django 4.2.17 on 2024-12-24 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0002_rename_user_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('OrderStatus', models.CharField(choices=[('in_progress', 'В процессе'), ('completed', 'Завершен'), ('cancelled', 'Отменен')], max_length=255)),
                ('OrderTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.users')),
            ],
        ),
    ]
