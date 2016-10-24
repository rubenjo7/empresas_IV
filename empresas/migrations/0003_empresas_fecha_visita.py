# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_remove_empresas_fecha_visita'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='fecha_visita',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 7, 5, 44, 895463, tzinfo=utc), verbose_name=b'Fecha visita'),
            preserve_default=False,
        ),
    ]
