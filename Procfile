release: python manage.py migrate --no-input
web: gunicorn csv_generator.wsgi
worker: celery -A csv_generator.celery worker -B --loglevel=info
