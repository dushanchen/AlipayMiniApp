# Generated by Django 2.1 on 2019-09-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190903_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alipay_user_id',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
