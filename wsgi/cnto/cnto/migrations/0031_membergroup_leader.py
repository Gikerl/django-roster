# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnto', '0030_remove_dts'),
    ]

    operations = [
        migrations.AddField(
            model_name='membergroup',
            name='leader',
            field=models.ForeignKey(default=None, to='cnto.Member', null=True),
        ),
    ]
