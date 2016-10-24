# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_empresas_fecha_visita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresas',
            name='fecha_visita',
        ),
    ]
