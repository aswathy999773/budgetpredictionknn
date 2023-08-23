# Generated by Django 3.2.18 on 2023-06-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contract_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('place', models.CharField(max_length=90)),
                ('postoffice', models.CharField(max_length=90)),
                ('district', models.CharField(max_length=90)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=90)),
                ('date', models.DateField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=90)),
                ('work', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=90)),
                ('date', models.DateField(max_length=90)),
                ('area', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('place', models.CharField(max_length=90)),
                ('postoffice', models.CharField(max_length=90)),
                ('district', models.CharField(max_length=90)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=90)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.login')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=90)),
                ('report', models.FileField(upload_to='')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.contract_company')),
                ('wid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.work')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('details', models.CharField(max_length=90)),
                ('price', models.BigIntegerField()),
                ('qty', models.CharField(max_length=90)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=90)),
                ('lname', models.CharField(max_length=90)),
                ('place', models.CharField(max_length=90)),
                ('postoffice', models.CharField(max_length=90)),
                ('pin', models.BigIntegerField()),
                ('phoneno', models.BigIntegerField()),
                ('department', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=90)),
                ('district', models.CharField(max_length=90)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.login')),
            ],
        ),
        migrations.CreateModel(
            name='instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(max_length=90)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.contract_company')),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.officer')),
            ],
        ),
        migrations.CreateModel(
            name='contractorrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=90)),
                ('request', models.CharField(max_length=90)),
                ('status', models.CharField(max_length=90)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.contract_company')),
                ('wid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.work')),
            ],
        ),
        migrations.AddField(
            model_name='contract_company',
            name='lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.login'),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('date', models.DateField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid', to='budget.login')),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tid', to='budget.login')),
            ],
        ),
    ]