# Generated by Django 3.1.6 on 2021-04-10 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_remove_contact_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='doctor',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(default='Self', max_length=40)),
                ('date_of_report', models.DateField(blank=True)),
                ('report_status', models.CharField(default='Pending', max_length=10)),
                ('report_img', models.ImageField(null=True, upload_to='')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.contact')),
            ],
        ),
    ]