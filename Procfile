web: gunicorn csv_generator.wsgi --log-file -
worker: celery -A csv_generator worker -B --loglevel=info
python manage.py celeryd -v 2 -B -s celery -E -l INFO
