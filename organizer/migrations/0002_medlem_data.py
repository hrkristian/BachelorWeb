# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-10 20:00
from __future__ import unicode_literals

from django.db import migrations, models

MEDLEMMER = [
    {
        "name":"Kristian Robertsen",
        "slug":"kristian",
        "contact":"kristian.robertsen@gmail.com"
    },
    {
        "name":"Nikolai Fosså",
        "slug":"nikolai",
        "contact":"nikolai.fossaa@gmail.com"
    },
    {
        "name":"Atle Amundsen",
        "slug":"atle",
        "contact":"brukerfeil72@gmail.com"
    }
]
def add_medlem_data(apps, schema_editor):
    Medlem = apps.get_model('organizer', 'Medlem')
    for medlem_dict in MEDLEMMER:
        medlem = Medlem.objects.create(
            name=medlem_dict['name'],
            slug=medlem_dict['slug'],
            contact=medlem_dict['contact']
        )
        medlem.save()

def remove_medlem_data(apps, schema_editor):
    Medlem = apps.get_model('organizer', 'Medlem')
    for medlem_dict in MEDLEMMER:
        medlem = Medlem.objects.get(
            slug=medlem_dict['slug']
        )
        medlem.delete()

class Migration(migrations.Migration):
    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_medlem_data,
            remove_medlem_data
        )
    ]
