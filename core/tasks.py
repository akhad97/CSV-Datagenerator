from __future__ import absolute_import, unicode_literals

from celery import shared_task

import csv
from faker import Faker
from .models import Scheme
import datetime
import os
from os import path
from pathlib import Path
from csv_generator.settings import *

from celery_progress.backend import ProgressRecorder

from time import sleep




@shared_task(bind=True)
def datagenerate(self, records, columns, names, filename, scheme_id):

    scheme = Scheme.objects.get(id=scheme_id)
    scheme.upload = 'In Progress'
    scheme.save()

    # Progress recorder

    sleep(1)

    progress_recorder = ProgressRecorder(self)
    for i in range(records):
        progress_recorder.set_progress(i + 1, records, f'Row {i} out of {records}')

    # Data for CSV
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # adding phone number

    filename_ = filename

    # writing rows
    with open(filename_, 'w') as csvFile:
        writer = csv.writer(csvFile)
        if names:
            writer.writerow(names)

        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()


    return filename + ' have been generated!'
